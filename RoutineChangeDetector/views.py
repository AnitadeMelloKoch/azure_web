from django.shortcuts import render
from django.http import HttpResponse
from .models import UserData, UserRoutine

# Create your views here.
def index(request):
    # print(request.POST['id'])
    return HttpResponse("Hello, world. You're at the RoutineChangeDetector index.")

def other(request):
    c = UserData.objects.all().count()
    print(c)
    return HttpResponse("This is another index:\n There are " + str(c) + " records" )

def posttest(request):
    print(request.POST)
    return HttpResponse(request.POST['data'])
