from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer #, RecieveDataSerialiser

# from .locationMath import get_location_data, get_quick_location_data
# from .statistics import * 
# import numpy
from .inference.inferenceMLP import predict

@api_view(['GET', 'POST'])
def user_data_list(request):
    """
    GET: List all UserData entries.

    POST: returns the posted data after processing.
    """
    if request.method == 'GET':
        user_data = UserData.objects.all()
        serializer = UserDataSerializer(user_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        values_maxtrix = []

        for data in request.data:
            model = UserData(data)
            serializer = UserDataSerializer(model)
            if serializer.is_valid:
                # model.save()
                values_maxtrix.append(list(serializer.data.values())[3:])
            else:
                return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        # print(values_maxtrix)
        result = predict(values_maxtrix, 'D:\\nicho\\Documents\\RoutineChangeDetector\\azure_web\\RoutineChangeDetector\\inference\\model-1000.meta', \
            'D:\\nicho\\Documents\\RoutineChangeDetector\\azure_web\\RoutineChangeDetector\\inference\\model-1000', False)
        # print(result)
        return Response({'classification': result}, status=status.HTTP_200_OK)
