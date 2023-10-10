from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from . import models

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
            'email':{'required': True}
        }
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name', 'email')
        
class UserPregnancyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPregnancyInfo
        fields = ('id','user','weight','height','weeks_pregnant')

class UserMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserMood
        fields = ('id','user','mood','date')