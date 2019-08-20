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
        for data in request.data:
            model = UserData()
            model.setValues(data)
            serializer = UserDataSerializer(model)
            if serializer.is_valid:
                # model.save()
                values_matrix.append(list(serializer.data.values())[3:])
            else:
                return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # values_matrix = np.loadtxt(open("D:\\nicho\Documents\RoutineChangeDetector\\app\ExtraSensory.per_uuid_features_labels\9DC38D04-E82E-4F29-AB52-B476535226F2.features_labels.csv", "rb"), delimiter=",", skiprows=1)
        # values_matrix = values_matrix[:1440,1:-52]
        standardized_values_matrix = standardize_features(values_matrix)
        result = predict(standardized_values_matrix, os.environ["META_DIR"], os.environ["CHKPNT_DIR"], False)
        print(result[0])
        labels = ["lying down","sitting","walking","running","bicycling","sleeping","driving (driver)","driving (pass)","exercise","shopping", "strolling", \
            "stairs (up)","stairs (down)","standing","lab work","in class","in meeting","cooking","drinking alcohol","shower","cleaning","laundry","washing dishes",\
                "watching TV","surfing Internet","singing","talking","computer work","eating","toilet","grooming","dressing","with coworker", "with friends",\
                    "main workplace","indoors","outdoors","in car","on bus","home","restaurant","atParty","atBar",'beach','atGym',"elevator","atSchool"]
        response = {
            'labels': labels, 
            'classification': result
        }
        return Response( response , status=status.HTTP_200_OK)
