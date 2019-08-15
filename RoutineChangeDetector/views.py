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

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer

@csrf_exempt
def user_data_list(request):
    """
    GET: List all UserData entries.

    POST: Prints the posted data.
    """
    if request.method == 'GET':
        user_data = UserData.objects.all()
        serializer = UserDataSerializer(user_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        return HttpResponse(request)
        # data = JSONParser().parse(request)
        # print(data)
        # return JsonResponse(data, status=201)
