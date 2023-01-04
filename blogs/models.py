from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    discription = models.CharField(max_length=255,null=True,blank=True)
    

class Blogs(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Categories,null=True,blank=True,on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    updated_at = models.DateTimeField(default=datetime.now(), blank=None, null=None)


class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now(), blank=None, null=None)


class Likes(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now(), blank=None, null=None)
