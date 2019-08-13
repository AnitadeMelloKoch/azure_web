from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # print(request.POST['id'])
    return HttpResponse("Hello, world. You're at the RoutineChangeDetector index.")
def other(request):
    return HttpResponse("This is another index: ")
