from .models import UserData, UserRoutine
from rest_framework import serializers

from .commModels import RecieveData

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class UserRoutineSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = UserRoutine
        fields = '__all__'

class RecieveDataSerialiser(serializers.ModelSerializer):
    class Meta:
        model = RecieveData
        fields = '__all__'