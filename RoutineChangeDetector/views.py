# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import UserData, UserRoutine

# # Create your views here.
# def index(request):
#     # print(request.POST['id'])
#     return HttpResponse("Hello, world. You're at the RoutineChangeDetector index.")

# def other(request):
#     c = UserData.objects.all().count()
#     print(c)
#     return HttpResponse("This is another index:\n There are " + str(c) + " records" )

# def posttest(request):
#     print(request.POST)
#     return HttpResponse(request.POST['data'])

# from .serializers import UserDataSerializer, UserRoutineSerializer
# from rest_framework import generics
# class GetDataView(generics.ListAPIView):
#     queryset = UserData.objects.all()
#     serializer_class = UserDataSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer, RecieveDataSerialiser

import json

@api_view(['GET', 'POST'])
def user_data_list(request):
    """
    GET: List all UserData entries.

    POST: Prints the posted data.
    """
    if request.method == 'GET':
        user_data = UserData.objects.all()
        serializer = UserDataSerializer(user_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        print(type(request.data))
        print(request.data["network"])
        serializer = RecieveDataSerialiser(data=request.data)
        if serializer.is_valid() :
            return Response(request.data["network"], status=status.HTTP_200_OK)
        else: 
            return Response(serializer.data, status=status.HTTP_501_NOT_IMPLEMENTED)
        # serializer = RecieveDataSerialiser(data=request.data)
        # if serializer.is_valid() :
        #     print(serializer)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
       
