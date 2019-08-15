from .models import UserData, UserRoutine
from rest_framework import serializers

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class UserRoutineSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = UserRoutine
        fields = '__all__'

class DataRecieveSerialiser(serializers.Serializer):
    dictionary = serializers.DictField