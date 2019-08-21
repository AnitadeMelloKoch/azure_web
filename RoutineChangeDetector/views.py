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
        values_matrix = []
        dataModels = []
        routineModels = []
        response = {
            'labels': [],
            'timestamps': [] 
        }
        strData = request.data["recordData"]
        # print(strData)
        recData = json.loads(strData)
        uuid = recData[0]["uuid"]
        for data in recData:
            # print(data)
            model = UserData() 
            model.setValues(data)
            response["timestamps"].append(model.timestamp)
            serializer = UserDataSerializer(model)
            if serializer.is_valid:
                # print(serializer.data)
                model.save()
                print("Saved Data")
                values_matrix.append(list(serializer.data.values())[3:])
                dataModels.append(model)
                routineModel = UserRoutine()
                UserRoutine.objects.get_or_create()
                routineModel.initialise(model.uuid, model, data["day"], data["hour"], data["minute"])
                routineSerializer = UserRoutineSerializer(routineModel)
                if routineSerializer.is_valid:
                    routineModel.save()
                    print("Saved Routine Instance")
                    routineModels.append(routineModel)
                else:
                    return Response(routineSerializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # values_matrix = np.loadtxt(open("D:\\nicho\Documents\RoutineChangeDetector\\app\ExtraSensory.per_uuid_features_labels\9DC38D04-E82E-4F29-AB52-B476535226F2.features_labels.csv", "rb"), delimiter=",", skiprows=1)
        # values_matrix = values_matrix[:1440,1:-52]
        standardized_values_matrix = standardize_features(values_matrix)
        predict_result = predict(standardized_values_matrix, os.environ["META_DIR"], os.environ["CHKPNT_DIR"], False)
        labels = np.asarray(["lying down","sitting","walking","running","bicycling","sleeping","driving (driver)","driving (pass)","exercise","shopping", "strolling", \
            "stairs (up)","stairs (down)","standing","lab work","in class","in meeting","cooking","drinking alcohol","shower","cleaning","laundry","washing dishes",\
                "watching TV","surfing Internet","singing","talking","computer work","eating","toilet","grooming","dressing","with coworker", "with friends",\
                    "main workplace","indoors","outdoors","in car","on bus","home","restaurant","at a party","at a bar",'beach','at the gym',"elevator","at school"])
        
        for idx, routineModel in enumerate(routineModels):
            # oldest at top
            routineModel.updatePredictions(predict_result[idx])
            routineModel.save()
        for i in range(len(predict_result)):
            response["labels"].append(getLabelsofMax(predict_result[0], labels))
        print("Done Prediction")

        RoutineQuerySet = UserRoutine.objects.filter(uuid=uuid)
        numRecords = UserRoutine.objects.filter(uuid=uuid).count()
        print(uuid, numRecords)
        if numRecords < 10:
            # set as not anomaly
            print("Not enough records for anomaly detection")
            for record in RoutineQuerySet.filter(anomaly=None):
                print("Setting as not anomaly")
                record.setAnomaly(False)
        else:
            # Run Inference
            print("Enough records to run inference")
            pass


        return Response( response , status=status.HTTP_200_OK)


def getLabelsofMax(arr1, arr2): 
    return arr2[arr1>0.9]