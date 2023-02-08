from asyncio import tasks
from dataclasses import field, fields
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from .models import Blogs

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'