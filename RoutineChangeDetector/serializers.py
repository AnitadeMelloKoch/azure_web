from .models import UserData, UserRoutine
from rest_framework import serializers

# from .commModels import RecieveData

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class UserRoutineSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserRoutine
        fields = '__all__'
