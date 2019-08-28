from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer #, RecieveDataSerialiser

# from .locationMath import get_d_model.location_data, get_quick_d_model.location_data
# from .statistics import * 
import os
import numpy as np
from .inference.inferenceMLP import predict
from .inference.format_data import standardize_features
from .inference.svm_app import detect_anomaly
import json
from datetime import datetime, timedelta

@api_view(['GET', 'POST'])
def user_data_list(request):
    """
    GET: List all UserData entries.

    POST: returns the posted data after processing.
    """
    if request.method == 'GET':
        user_data = UserData.objects.all()
        serializer = UserDataSerializer(user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        print("Starting saving data to db")
        strData = request.data["recordData"]
        recData = json.loads(strData)
        if len(recData) == 0:
            return Response({'success':False}, status=status.HTTP_204_NO_CONTENT)
        uuid = recData[0]["uuid"]
        model_list = []
        for idx, data in enumerate(recData):
            print("Entry", idx)
            copy = False
            for model in model_list:
                if(model.timestamp == data["timestamp"]):
                    copy = True
                    break
            if copy == True:
                continue
            model = UserData()
            model.setValues(data)
            srlzr = UserDataSerializer(model)
            if srlzr.is_valid:
                try:
                    UserData.objects.get(record_id=model.record_id)
                except UserData.DoesNotExist:
                    print("Creating new Model")
                    model_list.append(model)
            else: 
                return Response(srlzr.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            UserData.objects.bulk_create(model_list)
            print("Success")
            return Response({'success':True}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'success':False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def predict_actions(request):
    if request.method == 'GET':
        uuid = request.query_params.get('uuid', None)
        print(uuid)
        print("Getting Lists from database.")
        unpredicted_data_qs = UserData.objects.filter(uuid=uuid, classified=False).order_by('timestamp')
        unpredicted_data_length = unpredicted_data_qs.count()
        if unpredicted_data_length == 0:
            return Response({'success': False}, status=status.HTTP_204_NO_CONTENT)
        predicted_data_qs = UserData.objects.filter(uuid=uuid, classified=True).order_by('timestamp')
        predicted_data_length = min(predicted_data_qs.count(), 3*96)

        unpredicted_data_list = list(unpredicted_data_qs.values_list())
        predicted_data_list = list(predicted_data_qs.values_list()[:predicted_data_length])

        unpredicted_data = []
        for q in unpredicted_data_list:
            p = list(q)[4:]
            unpredicted_data.append(p)
        predicted_data = []
        for q in predicted_data_list:
            p = list(q)[4:]
            predicted_data.append(p)       
        full_list = predicted_data + unpredicted_data

        print("Normalizing based off " + str(predicted_data_length) + " previous datapoints.")
        normalized_full_list = standardize_features(full_list)
        normalized_unpredicted_list = normalized_full_list[-unpredicted_data_length:]
        normalized_unpredicted_length = len(normalized_unpredicted_list)
        
        print("Running Prediction")
        prediction_result = predict(normalized_unpredicted_list, os.environ["META_DIR"], os.environ["CHKPNT_DIR"], False)
        labels = np.asarray(["lying down","sitting","walking","running","bicycling","sleeping","driving (driver)","driving (pass)","exercise","shopping", "strolling", \
            "stairs (up)","stairs (down)","standing","lab work","in class","in meeting","cooking","drinking alcohol","shower","cleaning","laundry","washing dishes",\
                "watching TV","surfing Internet","singing","talking","computer work","eating","toilet","grooming","dressing","with coworker", "with friends",\
                    "main workplace","indoors","outdoors","in car","on bus","home","restaurant","at a party","at a bar",'beach','at the gym',"elevator","at school"])
        
        routine_model_list = []
        prediction_label_list = []
        timestamp_list = []
        print("Creating Models for Results")
        for idx, prediction in enumerate(prediction_result):
            prediction_label_list.append(getLabelsofMax(prediction, labels))
            timestamp = unpredicted_data_list[idx][2]
            timestamp_list.append(timestamp)
            r_model = UserRoutine()
            d_model = unpredicted_data_qs[idx]
            dt = datetime.fromtimestamp(timestamp/1000.0)
            day = float(dt.strftime("%w"))
            hour = float(dt.strftime("%-H"))
            minute = float(dt.strftime("%-M"))
            r_model.initialise(uuid, timestamp, d_model, day, hour, minute)
            r_model.updatePredictions(prediction)
            r_srlzr = UserRoutineSerializer(r_model)
            if r_srlzr.is_valid:
                try:
                    UserRoutine.objects.get(routine_id=r_model.routine_id)
                except UserRoutine.DoesNotExist:
                    routine_model_list.append(r_model)
            else:
                return Response(r_srlzr.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            unpredicted_data_qs.update(classified=True)
            UserRoutine.objects.bulk_create(routine_model_list)
            print('Success')
            return Response({'success':True, 'activity_labels': prediction_label_list, 'timestamps':timestamp_list}, status=status.HTTP_200_OK)
        except:
            return Response({'success':False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def detect_anomalies(request):
    if request.method == 'GET':
        uuid = request.query_params.get('uuid', None)
        print(uuid)
        print("Get points from database")
        undetected_data_qs = UserRoutine.objects.filter(uuid=uuid, anomaly=None).order_by('timestamp')
        undetected_data_length = undetected_data_qs.count()
        if undetected_data_length == 0:
            return Response({'success':False}, status=status.HTTP_204_NO_CONTENT)
        nonanomolous_data_qs = UserRoutine.objects.filter(uuid=uuid, anomaly=False)
        if nonanomolous_data_qs.count() < 1344:
            undetected_data_qs.update(anomaly=False)
            print("Not enough points for anomaly detection " + str(nonanomolous_data_qs.count()))
            return Response({'success':True, 'information':'Not enough points for anomaly detection'}, status=status.HTTP_202_ACCEPTED)
        undetected_data_list = list(undetected_data_qs.values_list())
        nonanomolous_data_list = list(nonanomolous_data_qs.values_list())

        undetected_data = []
        nonanomolous_data = []
        for q in undetected_data_list:
            p = list(q)[4:-1]
            undetected_data.append(p)
        for q in nonanomolous_data_list:
            p = list(q)[4:-1]
            nonanomolous_data.append(p)
        
        print("Detecting anomalies")
        anomaly_result = detect_anomaly(nonanomolous_data, undetected_data)

        print("Update model with results")
        try:
            for idx, result in enumerate(anomaly_result):
                if result == 1:
                    model = UserRoutine.objects.get(routine_id=undetected_data_list[idx][0])
                    model.anomaly=True
                    model.save()
                else:
                    model = UserRoutine.objects.get(routine_id=undetected_data_list[idx][0])
                    model.anomaly=False
                    model.save()

            print('Success')
            return Response({'success': True}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_user_anomalies(request):
    """
    GET: Gets anomaly details from index [start, end). start inclusive, end exclusive. If no start, start = 0, if no end, end = number of records in database 
    """
    if request.method == 'GET':
        uuid = request.query_params.get('uuid', None)
        start = int(request.query_params.get('start', 0))
        end = int(request.query_params.get('end', -1))
        if end == -1:
            end = int(UserRoutine.objects.filter(uuid=uuid).count())
        
        if end < start:
            return Response({'success': False, 'message': 'End cannot be before start.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        print("Getting list from database")
        data_qs = UserRoutine.objects.filter(uuid=uuid).order_by('-timestamp')
        wanted_data_qs = data_qs[start:end]
        wanted_data_list = list(wanted_data_qs.values_list())

        wanted_data = []
        for q in wanted_data_list:
            p = list(q)[7:-1]
            wanted_data.append(p)
        anomaly = []
        for q in wanted_data_list:
            p = list(q)[-1]
            anomaly.append(p)
        timestamps = []
        for q in wanted_data_list:
            p = list(q)[2]
            timestamps.append(p)

        labels = np.asarray(["lying down","sitting","walking","running","bicycling","sleeping","driving (driver)","driving (pass)","exercise","shopping", "strolling", \
            "stairs (up)","stairs (down)","standing","lab work","in class","in meeting","cooking","drinking alcohol","shower","cleaning","laundry","washing dishes",\
                "watching TV","surfing Internet","singing","talking","computer work","eating","toilet","grooming","dressing","with coworker", "with friends",\
                    "main workplace","indoors","outdoors","in car","on bus","home","restaurant","at a party","at a bar",'beach','at the gym',"elevator","at school"])
        
        activity_label_list = []
        for idx, activities in enumerate(wanted_data):
            a_arr = np.asarray(activities)
            activity_label_list.append(getLabelsofMax(a_arr, labels))

        return Response({'success': True, 'activity_labels': activity_label_list, 'timestamps':timestamps, 'anomaly':anomaly, 'length': len(activity_label_list)}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_record_num(request):
    if request.method == 'GET':
        uuid = request.query_params.get('uuid', None)
        data_qs = UserRoutine.objects.filter(uuid=uuid)
        num_record = data_qs.count()
        

        return Response({'success':True, 'num_records':num_record}, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_classification_info(request):
    if request.method == 'POST':
        print("Updating Record")
        uuid = request.data["uuid"]
        timestampStr = request.data["timestamp"]
        timestamp = float(timestampStr)
        new_activity_arr = json.loads(request.data["activityArr"])
        new_anomaly = True if request.data["anomaly"] == 'true' else False
        try:
            model = UserRoutine.objects.get(routine_id=uuid+str(timestampStr))
            model.updatePredictions(new_activity_arr)
            model.setAnomaly(new_anomaly)
            if UserRoutineSerializer(model).is_valid:
                model.save()
                print("Updated Entry")
                return Response({'success': True}, status=status.HTTP_200_OK)
            else:
                return Response({'success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'success':False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def detect_one_anomaly(request):
    uuid = request.query_params.get('uuid', None)
    timestamp = int(request.query_params.get('timestamp', None))
    print("Detecting Anomaly on " + uuid + str(timestamp))
    try:
        model = UserRoutine.objects.get(routine_id=uuid + str(timestamp))
        nonanomolous_data_qs = UserRoutine.objects.filter(uuid=uuid, anomaly=False)
        if nonanomolous_data_qs.count() < 1344:
            model.anomaly = False
            model.save()
            print("Not enough points for anomaly detection " + str(nonanomolous_data_qs.count()))
            return Response({'success':True, 'information':'Not enough points for anomaly detection'}, status=status.HTTP_202_ACCEPTED)
        record_list = [[model.day, model.hour, model.minute, model.lying_down, model.sitting, model.walking, model.running, model.bicycling, model.sleeping, model.driving_driver, model.driving_pass, model.exercise, model.shopping, model.strolling , model.stairs_up, model.stairs_down, model.standing, model.lab_work, model.in_class, model.in_meeting, model.cooking, model.drinking_alcohol, model.shower, model.cleaning, model.laundry, model.washing_dishes, model.watch_tv, model.surf_internet, model.singing, model.talking, model.computer_work, model.eating, model.toilet, model.grooming, model.dressing, model.with_coworker, model.with_friends, model.main_workplace, model.indoors, model.outdoors, model.in_car, model.on_bus, model.home, model.restaurant, model.at_party, model.at_bar, model.beach, model.at_gym, model.elevator, model.at_school]]
        nonanomolous_data_list = list(nonanomolous_data_qs.values_list())
        nonanomolous_data = []
        for q in nonanomolous_data_list:
            p = list(q)[4:-1]
            nonanomolous_data.append(p)
        print("Detecting Anomaly")
        anomaly_result = detect_anomaly(nonanomolous_data, record_list)
        print("Updating Model")
        try:
            if anomaly_result[0] == 1:
                model.anomaly = True
            else:
                model.anomaly = False
            model.save()
            print("Successs")
            return Response({'success': True, 'anomaly': model.anomaly}, status=status.HTTP_200_OK)    
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def getLabelsofMax(arr1, arr2): 
    return arr2[arr1>0.9]


from .read_data import *
@api_view(['GET'])
def import_fake_data(request):
    print("Adding fake data for uuid 70dcabedc6d7d3ee")
    uuid = "70dcabedc6d7d3ee"
    # dt = datetime.strptime('2019-07-01 00:15:00', '%Y-%m-%d %H:%M:%S')
    dt = datetime.strptime('2019-07-29 00:15:00', '%Y-%m-%d %H:%M:%S')

    non_anomaly_data_matrix = read_data('/mnt/d/nicho/Documents/RoutineChangeDetector/azure_web/fakedata/haveAnom.csv')
    d_model_list = []
    r_model_list = []
    for idx, non_anomaly_record in enumerate(non_anomaly_data_matrix):
        print(dt)
        # print(idx)
        timestamp = datetime.timestamp(dt) * 1000
        

        d_model = UserData()
        d_model.record_id= uuid + str(int(timestamp))
        d_model.uuid = uuid
        d_model.timestamp = int(timestamp)
        d_model.classified = True 
        d_model.raw_acc_magnitude_stats_mean = 0
        d_model.raw_acc_magnitude_stats_std = 0
        d_model.raw_acc_magnitude_stats_moment3 = 0
        d_model.raw_acc_magnitude_stats_moment4 = 0
        d_model.raw_acc_magnitude_stats_percentile25 = 0
        d_model.raw_acc_magnitude_stats_percentile50 = 0
        d_model.raw_acc_magnitude_stats_percentile75 = 0
        d_model.raw_acc_magnitude_stats_value_entropy = 0
        d_model.raw_acc_magnitude_stats_time_entropy = 0
        d_model.raw_acc_magnitude_spectrum_log_energy_band0 = 0
        d_model.raw_acc_magnitude_spectrum_log_energy_band1 = 0
        d_model.raw_acc_magnitude_spectrum_log_energy_band2 = 0
        d_model.raw_acc_magnitude_spectrum_log_energy_band3 = 0
        d_model.raw_acc_magnitude_spectrum_log_energy_band4 = 0
        d_model.raw_acc_magnitude_spectrum_spectral_entropy = 0
        d_model.raw_acc_magnitude_autocorrelation_period = 0
        d_model.raw_acc_magnitude_autocorrelation_normalized_ac = 0
        d_model.raw_acc_3d_mean_x = 0
        d_model.raw_acc_3d_mean_y = 0
        d_model.raw_acc_3d_mean_z = 0
        d_model.raw_acc_3d_std_x = 0
        d_model.raw_acc_3d_std_y = 0
        d_model.raw_acc_3d_std_z = 0
        d_model.raw_acc_3d_ro_xy = 0
        d_model.raw_acc_3d_ro_xz = 0
        d_model.raw_acc_3d_ro_yz = 0
        d_model.proc_gyro_magnitude_stats_mean = 0
        d_model.proc_gyro_magnitude_stats_std = 0
        d_model.proc_gyro_magnitude_stats_moment3 = 0
        d_model.proc_gyro_magnitude_stats_moment4 = 0
        d_model.proc_gyro_magnitude_stats_percentile25 = 0
        d_model.proc_gyro_magnitude_stats_percentile50 = 0
        d_model.proc_gyro_magnitude_stats_percentile75 = 0
        d_model.proc_gyro_magnitude_stats_value_entropy = 0
        d_model.proc_gyro_magnitude_stats_time_entropy = 0
        d_model.proc_gyro_magnitude_spectrum_log_energy_band0 = 0
        d_model.proc_gyro_magnitude_spectrum_log_energy_band1 = 0
        d_model.proc_gyro_magnitude_spectrum_log_energy_band2 = 0
        d_model.proc_gyro_magnitude_spectrum_log_energy_band3 = 0
        d_model.proc_gyro_magnitude_spectrum_log_energy_band4 = 0
        d_model.proc_gyro_magnitude_spectrum_spectral_entropy = 0
        d_model.proc_gyro_magnitude_autocorrelation_period = 0
        d_model.proc_gyro_magnitude_autocorrelation_normalized_ac = 0
        d_model.proc_gyro_3d_mean_x = 0
        d_model.proc_gyro_3d_mean_y = 0
        d_model.proc_gyro_3d_mean_z = 0
        d_model.proc_gyro_3d_std_x = 0
        d_model.proc_gyro_3d_std_y = 0
        d_model.proc_gyro_3d_std_z = 0
        d_model.proc_gyro_3d_ro_xy = 0
        d_model.proc_gyro_3d_ro_xz = 0
        d_model.proc_gyro_3d_ro_yz = 0
        d_model.raw_magnet_magnitude_stats_mean = 0
        d_model.raw_magnet_magnitude_stats_std = 0
        d_model.raw_magnet_magnitude_stats_moment3 = 0
        d_model.raw_magnet_magnitude_stats_moment4 = 0
        d_model.raw_magnet_magnitude_stats_percentile25 = 0
        d_model.raw_magnet_magnitude_stats_percentile50 = 0
        d_model.raw_magnet_magnitude_stats_percentile75 = 0
        d_model.raw_magnet_magnitude_stats_value_entropy = 0
        d_model.raw_magnet_magnitude_stats_time_entropy = 0
        d_model.raw_magnet_magnitude_spectrum_log_energy_band0 = 0
        d_model.raw_magnet_magnitude_spectrum_log_energy_band1 = 0
        d_model.raw_magnet_magnitude_spectrum_log_energy_band2 = 0
        d_model.raw_magnet_magnitude_spectrum_log_energy_band3 = 0
        d_model.raw_magnet_magnitude_spectrum_log_energy_band4 = 0
        d_model.raw_magnet_magnitude_spectrum_spectral_entropy = 0
        d_model.raw_magnet_magnitude_autocorrelation_period = 0
        d_model.raw_magnet_magnitude_autocorrelation_normalized_ac = 0
        d_model.raw_magnet_3d_mean_x = 0
        d_model.raw_magnet_3d_mean_y = 0
        d_model.raw_magnet_3d_mean_z = 0
        d_model.raw_magnet_3d_std_x = 0
        d_model.raw_magnet_3d_std_y = 0
        d_model.raw_magnet_3d_std_z = 0
        d_model.raw_magnet_3d_ro_xy = 0
        d_model.raw_magnet_3d_ro_xz = 0
        d_model.raw_magnet_3d_ro_yz = 0
        d_model.raw_magnet_avr_cosine_similarity_lag_range0 = 0
        d_model.raw_magnet_avr_cosine_similarity_lag_range1 = 0
        d_model.raw_magnet_avr_cosine_similarity_lag_range2 = 0
        d_model.raw_magnet_avr_cosine_similarity_lag_range3 = 0
        d_model.raw_magnet_avr_cosine_similarity_lag_range4 = 0
        d_model.watch_acc_magnitude_stats_mean = 0
        d_model.watch_acc_magnitude_stats_std = 0
        d_model.watch_acc_magnitude_stats_moment3 = 0
        d_model.watch_acc_magnitude_stats_moment4 = 0
        d_model.watch_acc_magnitude_stats_percentile25 = 0
        d_model.watch_acc_magnitude_stats_percentile50 = 0
        d_model.watch_acc_magnitude_stats_percentile75 = 0
        d_model.watch_acc_magnitude_stats_value_entropy = 0
        d_model.watch_acc_magnitude_stats_time_entropy = 0
        d_model.watch_acc_magnitude_spectrum_log_energy_band0 = 0
        d_model.watch_acc_magnitude_spectrum_log_energy_band1 = 0
        d_model.watch_acc_magnitude_spectrum_log_energy_band2 = 0
        d_model.watch_acc_magnitude_spectrum_log_energy_band3 = 0
        d_model.watch_acc_magnitude_spectrum_log_energy_band4 = 0
        d_model.watch_acc_magnitude_spectrum_spectral_entropy = 0
        d_model.watch_acc_magnitude_autocorrelation_period = 0
        d_model.watch_acc_magnitude_autocorrelation_normalized_ac = 0
        d_model.watch_acc_3d_mean_x = 0
        d_model.watch_acc_3d_mean_y = 0
        d_model.watch_acc_3d_mean_z = 0
        d_model.watch_acc_3d_std_x = 0
        d_model.watch_acc_3d_std_y = 0
        d_model.watch_acc_3d_std_z = 0
        d_model.watch_acc_3d_ro_xy = 0
        d_model.watch_acc_3d_ro_xz = 0
        d_model.watch_acc_3d_ro_yz = 0
        d_model.watch_acc_spectrum_x_log_energy_band0 = 0
        d_model.watch_acc_spectrum_x_log_energy_band1 = 0
        d_model.watch_acc_spectrum_x_log_energy_band2 = 0
        d_model.watch_acc_spectrum_x_log_energy_band3 = 0
        d_model.watch_acc_spectrum_x_log_energy_band4 = 0
        d_model.watch_acc_spectrum_y_log_energy_band0 = 0
        d_model.watch_acc_spectrum_y_log_energy_band1 = 0
        d_model.watch_acc_spectrum_y_log_energy_band2 = 0
        d_model.watch_acc_spectrum_y_log_energy_band3 = 0
        d_model.watch_acc_spectrum_y_log_energy_band4 = 0
        d_model.watch_acc_spectrum_z_log_energy_band0 = 0
        d_model.watch_acc_spectrum_z_log_energy_band1 = 0
        d_model.watch_acc_spectrum_z_log_energy_band2 = 0
        d_model.watch_acc_spectrum_z_log_energy_band3 = 0
        d_model.watch_acc_spectrum_z_log_energy_band4 = 0
        d_model.watch_acc_relative_directions_avr_cosine_similarity_lag_range0 = 0
        d_model.watch_acc_relative_directions_avr_cosine_similarity_lag_range1 = 0
        d_model.watch_acc_relative_directions_avr_cosine_similarity_lag_range2 = 0
        d_model.watch_acc_relative_directions_avr_cosine_similarity_lag_range3 = 0
        d_model.watch_acc_relative_directions_avr_cosine_similarity_lag_range4 = 0
        d_model.watch_heading_mean_cos = 0
        d_model.watch_heading_std_cos = 0
        d_model.watch_heading_mom3_cos = 0
        d_model.watch_heading_mom4_cos = 0
        d_model.watch_heading_mean_sin = 0
        d_model.watch_heading_std_sin = 0
        d_model.watch_heading_mom3_sin = 0
        d_model.watch_heading_mom4_sin = 0
        d_model.watch_heading_entropy_8bins = 0
        d_model.location_num_valid_updates = 0
        d_model.location_log_latitude_range = 0
        d_model.location_log_longitude_range = 0
        d_model.location_min_altitude = 0
        d_model.location_max_altitude = 0
        d_model.location_min_speed = 0
        d_model.location_max_speed = 0
        d_model.location_best_horizontal_accuracy = 0
        d_model.location_best_vertical_accuracy = 0
        d_model.location_diameter = 0
        d_model.location_log_diameter = 0
        d_model.location_quick_features_std_lat = 0
        d_model.location_quick_features_std_long = 0
        d_model.location_quick_features_lat_change = 0
        d_model.location_quick_features_long_change = 0
        d_model.location_quick_features_mean_abs_lat_deriv = 0
        d_model.location_quick_features_mean_abs_long_deriv = 0
        d_model.audio_naive_mfcc0_mean = 0
        d_model.audio_naive_mfcc1_mean = 0
        d_model.audio_naive_mfcc2_mean = 0
        d_model.audio_naive_mfcc3_mean = 0
        d_model.audio_naive_mfcc4_mean = 0
        d_model.audio_naive_mfcc5_mean = 0
        d_model.audio_naive_mfcc6_mean = 0
        d_model.audio_naive_mfcc7_mean = 0
        d_model.audio_naive_mfcc8_mean = 0
        d_model.audio_naive_mfcc9_mean = 0
        d_model.audio_naive_mfcc10_mean = 0
        d_model.audio_naive_mfcc11_mean = 0
        d_model.audio_naive_mfcc12_mean = 0
        d_model.audio_naive_mfcc0_std = 0
        d_model.audio_naive_mfcc1_std = 0
        d_model.audio_naive_mfcc2_std = 0
        d_model.audio_naive_mfcc3_std = 0
        d_model.audio_naive_mfcc4_std = 0
        d_model.audio_naive_mfcc5_std = 0
        d_model.audio_naive_mfcc6_std = 0
        d_model.audio_naive_mfcc7_std = 0
        d_model.audio_naive_mfcc8_std = 0
        d_model.audio_naive_mfcc9_std = 0
        d_model.audio_naive_mfcc10_std = 0
        d_model.audio_naive_mfcc11_std = 0
        d_model.audio_naive_mfcc12_std = 0
        d_model.audio_properties_max_abs_value = 0
        d_model.audio_properties_normalization_multiplier = 0
        d_model.discrete_app_state_is_active = False
        d_model.discrete_app_state_is_inactive = False
        d_model.discrete_app_state_is_background = False
        d_model.discrete_app_state_missing = False
        d_model.discrete_battery_plugged_is_ac = False
        d_model.discrete_battery_plugged_is_usb = False
        d_model.discrete_battery_plugged_is_wireless = False
        d_model.discrete_battery_plugged_missing = False
        d_model.discrete_battery_state_is_unknown = False
        d_model.discrete_battery_state_is_unplugged = False
        d_model.discrete_battery_state_is_not_charging = False
        d_model.discrete_battery_state_is_discharging = False
        d_model.discrete_battery_state_is_charging = False
        d_model.discrete_battery_state_is_full = False
        d_model.discrete_battery_state_missing = False
        d_model.discrete_on_the_phone_is_False = False
        d_model.discrete_on_the_phone_is_True = False
        d_model.discrete_on_the_phone_missing = False
        d_model.discrete_ringer_mode_is_normal = False
        d_model.discrete_ringer_mode_is_silent_no_vibrate = False
        d_model.discrete_ringer_mode_is_silent_with_vibrate = False
        d_model.discrete_ringer_mode_missing = False
        d_model.discrete_wifi_status_is_not_reachable = False
        d_model.discrete_wifi_status_is_reachable_via_wifi = False
        d_model.discrete_wifi_status_is_reachable_via_wwan = False
        d_model.discrete_wifi_status_missing = False
        d_model.lf_measurements_light = 0
        d_model.lf_measurements_pressure = 0
        d_model.lf_measurements_proximity_cm = 0
        d_model.lf_measurements_proximity = 0
        d_model.lf_measurements_relative_humidity = 0
        d_model.lf_measurements_battery_level = 0
        d_model.lf_measurements_screen_brightness = 0
        d_model.lf_measurements_temperature_ambient = 0
        d_model.discrete_time_of_day_between0and6 = False
        d_model.discrete_time_of_day_between3and9 = False
        d_model.discrete_time_of_day_between6and12 = False
        d_model.discrete_time_of_day_between9and15 = False
        d_model.discrete_time_of_day_between12and18 = False
        d_model.discrete_time_of_day_between15and21 = False
        d_model.discrete_time_of_day_between18and24 = False
        d_model.discrete_time_of_day_between21and3 = False

        r_model = UserRoutine()
        r_model.routine_id = uuid + str(int(timestamp))
        r_model.uuid = uuid
        r_model.timestamp = int(timestamp)
        r_model.data_record = d_model
        r_model.day = non_anomaly_record[0]
        r_model.hour = non_anomaly_record[1]
        r_model.minute = non_anomaly_record[2]

        r_model.lying_down = bool(non_anomaly_record[3])
        r_model.sitting = bool(non_anomaly_record[4])
        r_model.walking = bool(non_anomaly_record[5])
        r_model.running = bool(non_anomaly_record[6])
        r_model.bicycling = bool(non_anomaly_record[7])
        r_model.sleeping = bool(non_anomaly_record[8])
        r_model.driving_driver = bool(non_anomaly_record[9])
        r_model.driving_pass = bool(non_anomaly_record[10])
        r_model.exercise = bool(non_anomaly_record[11])
        r_model.shopping = bool(non_anomaly_record[12])
        r_model.strolling = bool(non_anomaly_record[13]) 
        r_model.stairs_up = bool(non_anomaly_record[14])
        r_model.stairs_down = bool(non_anomaly_record[15])
        r_model.standing = bool(non_anomaly_record[16])
        r_model.lab_work = bool(non_anomaly_record[17])
        r_model.in_class = bool(non_anomaly_record[18])
        r_model.in_meeting = bool(non_anomaly_record[19])
        r_model.cooking = bool(non_anomaly_record[20])
        r_model.drinking_alcohol = bool(non_anomaly_record[21])
        r_model.shower = bool(non_anomaly_record[22])
        r_model.cleaning = bool(non_anomaly_record[23])
        r_model.laundry = bool(non_anomaly_record[24])
        r_model.washing_dishes = bool(non_anomaly_record[25])
        r_model.watch_tv = bool(non_anomaly_record[26])
        r_model.surf_internet = bool(non_anomaly_record[27])
        r_model.singing = bool(non_anomaly_record[28])
        r_model.talking = bool(non_anomaly_record[29])
        r_model.computer_work = bool(non_anomaly_record[30])
        r_model.eating = bool(non_anomaly_record[31])
        r_model.toilet = bool(non_anomaly_record[32])
        r_model.grooming = bool(non_anomaly_record[33])
        r_model.dressing = bool(non_anomaly_record[34])
        r_model.with_coworker = bool(non_anomaly_record[35])
        r_model.with_friends = bool(non_anomaly_record[36])
        r_model.main_workplace = bool(non_anomaly_record[37])
        r_model.indoors = bool(non_anomaly_record[38])
        r_model.outdoors = bool(non_anomaly_record[39])
        r_model.in_car = bool(non_anomaly_record[40])
        r_model.on_bus = bool(non_anomaly_record[41])
        r_model.home = bool(non_anomaly_record[42])
        r_model.restaurant = bool(non_anomaly_record[43])
        r_model.at_party = bool(non_anomaly_record[44])
        r_model.at_bar = bool(non_anomaly_record[45])
        r_model.beach = bool(non_anomaly_record[46])
        r_model.at_gym = bool(non_anomaly_record[47])
        r_model.elevator = bool(non_anomaly_record[48])
        r_model.at_school = bool(non_anomaly_record[49])
        r_model.anomaly = None#bool(non_anomaly_record[50]) ################################################## ! None


        d_srlzr = UserDataSerializer(d_model)
        r_srlzr = UserRoutineSerializer(r_model)

        if d_srlzr.is_valid and r_srlzr.is_valid:
            d_model_list.append(d_model)
            r_model_list.append(r_model)
        else:
            print(idx)
            return Response({'data': d_srlzr.errors, 'routine': r_srlzr.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        dt = dt + timedelta(minutes=15)

    try:
        UserData.objects.bulk_create(d_model_list)
        UserRoutine.objects.bulk_create(r_model_list)
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

