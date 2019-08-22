from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer #, RecieveDataSerialiser

# from .locationMath import get_location_data, get_quick_location_data
# from .statistics import * 
import os
import numpy as np
from .inference.inferenceMLP import predict
from .inference.format_data import standardize_features
import json
from datetime import datetime

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
        for data in recData:
            model = UserData()
            model.setValues(data)
            srlzr = UserDataSerializer(model)
            if srlzr.is_valid:
                try:
                    UserData.objects.get(record_id=model.record_id)
                except UserData.DoesNotExist:
                    model_list.append(model)
            else: 
                return Response(srlzr.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            UserData.objects.bulk_create(model_list)
            print("Success")
            return Response({'success':True}, status=status.HTTP_200_OK)
        except:
            return Response({'success':False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # values_matrix = []
        # dataModels = []
        # routineModels = []
        # response = {
        #     'labels': [],
        #     'timestamps': [] 
        # }
        # strData = request.data["recordData"]
        # # print(strData)
        # recData = json.loads(strData)
        # uuid = recData[0]["uuid"]
        # for data in recData:
        #     # print(data)
        #     model = UserData() 
        #     model.setValues(data)
        #     response["timestamps"].append(model.timestamp)
        #     serializer = UserDataSerializer(model)
        #     if serializer.is_valid:
        #         model.save()
        #         values_matrix.append(list(serializer.data.values())[3:])
        #         dataModels.append(model)
        #         routineModel = UserRoutine()
        #         routineModel.initialise(model.uuid, model.timestamp, model, data["day"], data["hour"], data["minute"])
        #         routineSerializer = UserRoutineSerializer(routineModel)
        #         if routineSerializer.is_valid:
        #             routineModel, created = UserRoutine.objects.get_or_create(routineModel.record_id, defaults=routineModel)
        #             if created:
        #                 print("Saved Routine Instance")
        #             else: 
        #                 print("Using Existing RoutineModel")
        #             routineModels.append(routineModel)
        #         else:
        #             return Response(routineSerializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        #     else:
        #         return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # # values_matrix = np.loadtxt(open("D:\\nicho\Documents\RoutineChangeDetector\\app\ExtraSensory.per_uuid_features_labels\9DC38D04-E82E-4F29-AB52-B476535226F2.features_labels.csv", "rb"), delimiter=",", skiprows=1)
        # # values_matrix = values_matrix[:1440,1:-52]
        # standardized_values_matrix = standardize_features(values_matrix)
        # predict_result = predict(standardized_values_matrix, os.environ["META_DIR"], os.environ["CHKPNT_DIR"], False)
        # labels = np.asarray(["lying down","sitting","walking","running","bicycling","sleeping","driving (driver)","driving (pass)","exercise","shopping", "strolling", \
        #     "stairs (up)","stairs (down)","standing","lab work","in class","in meeting","cooking","drinking alcohol","shower","cleaning","laundry","washing dishes",\
        #         "watching TV","surfing Internet","singing","talking","computer work","eating","toilet","grooming","dressing","with coworker", "with friends",\
        #             "main workplace","indoors","outdoors","in car","on bus","home","restaurant","at a party","at a bar",'beach','at the gym',"elevator","at school"])
        
        # for idx, routineModel in enumerate(routineModels):
        #     # oldest at top
        #     routineModel.updatePredictions(predict_result[idx])
        #     routineModel.save()
        # for i in range(len(predict_result)):
        #     response["labels"].append(getLabelsofMax(predict_result[0], labels))
        # print("Done Prediction")

        # RoutineQuerySet = UserRoutine.objects.filter(uuid=uuid)
        # numRecords = UserRoutine.objects.filter(uuid=uuid).count()
        # print(uuid, numRecords)
        # if numRecords < 10:
        #     # set as not anomaly
        #     print("Not enough records for anomaly detection")
        #     for record in RoutineQuerySet.filter(anomaly=None):
        #         print("Setting as not anomaly")
        #         record.setAnomaly(False)
        # else:
        #     # Run Inference
        #     print("Enough records to run inference")
        #     pass


        # return Response( response , status=status.HTTP_200_OK)

@api_view(['GET'])
def predict_actions(request):
    if request.method == 'GET':
        uuid = request.query_params.get('uuid', None)
        print(uuid)
        print("Getting Lists from database.")
        unpredicted_data_qs = UserData.objects.filter(uuid=uuid, classified=False).order_by('timestamp')
        unpredicted_data_length = unpredicted_data_qs.count()
        if unpredicted_data_length == 0:
            return Response({'success':False}, status=status.HTTP_204_NO_CONTENT)
        predicted_data_qs = UserData.objects.filter(uuid=uuid, classified=True).order_by('timestamp')
        predicted_data_length = min(predicted_data_qs.count(), 100)

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
            print(uuid, timestamp, d_model.timestamp, day, hour, minute)
            r_model.initialise(uuid, timestamp, d_model, day, hour, minute)
            r_srlzr = UserRoutineSerializer(r_model)
            if r_srlzr.is_valid:
                try:
                    UserRoutine.objects.get(routine_id=r_model.routine_id)
                except UserRoutine.DoesNotExist:
                    routine_model_list.append(r_model)
            else:
                return Response(r_srlzr.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            # unpredicted_data_qs.update(classified=True)
            # UserRoutine.objects.bulk_create(routine_model_list)
            print('Success')
            return Response({'success':True, 'activity_labels': prediction_label_list, 'timestamps':timestamp_list}, status=status.HTTP_200_OK)
        except:
            return Response({'success':False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            




        return Response({
            'uuid': uuid,
            'unpredicted_data': unpredicted_data,
            'normalized_unpredicted_data': normalized_unpredicted_list,
            'unpredicted_data_length': unpredicted_data_length,
            'normalized_unpredicted_length': normalized_unpredicted_length
            }, status=status.HTTP_200_OK)


def getLabelsofMax(arr1, arr2): 
    return arr2[arr1>0.9]