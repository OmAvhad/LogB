from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.
class UserPregnancyInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weeks_pregnant = models.IntegerField(null=True, blank=True)
    
class UserMood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now())