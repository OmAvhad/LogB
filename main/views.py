from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def home(request,template_name="main/home.html"):
    return render(request,template_name)

def login_template(request,template_name="main/login.html"):
    return render(request,template_name)

def about_template(request,template_name="main/about.html"):
    return render(request,template_name)

def register_template(request,template_name="main/register.html"):
    return render(request,template_name)

def logout_url(request):
    if request.method == "POST":
        try:
            logout(request)
            status="successful"
            status_code = 200
            message = "Logout Successful"
        except:
            status="failed"
            status_code = 400
            message = "Some error occured"
        return JsonResponse(Response(status=status,status_code=status_code,message=message))

# @csrf_protect
@csrf_exempt
def login_api(request):
    if request.method == "POST":
        postdata = request.POST
        username = postdata['username']
        password = postdata['password']
        try:
            user = authenticate(username=username, password=password)
        except:
            user = None
        if user is not None:
            login(request,user)
            status = 'successful'
            status_code = '200'
            message = 'Successfully loggedin!'
        else:
            status = 'failed'
            status_code = '400'
            message = 'User not found'
    return JsonResponse(Response(status=status,status_code=status_code,message=message))

# @csrf_protect
@csrf_exempt
def register_api(request):
    if request.method == "POST":
        postdata = request.POST
        try:
            username = postdata['username']
            password = make_password(postdata['password'])
            first_name = postdata['first_name']
            last_name = postdata['last_name']
            email = postdata['email']
            try:
                user = User.objects.get(Q(username=username) | Q(email=email))
            except:
                user = None
            if user ==  None:
                User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                status = 'successful'
                status_code = '200'
                message = 'User Registered Successfully'
            else:
                status = 'failed'
                status_code = '400'
                message = 'Username or Email already Exists.'
        except Exception as e:
            status = 'failed'
            status_code = '400'
            message = 'Send all required details.'
        
    return JsonResponse(Response(status=status,status_code=status_code,message=message))

def Response(status,status_code,data={},message = "",):
    response = {'status':status,'status_code':status_code,'data':data,'message':message}
    return response

from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from . import models

@csrf_exempt
def register(request):
    postdata = request.POST
    try:
        user = User.objects.filter(Q(username=postdata['email']) | Q(email=postdata['email'])).count()
    except:
        user = None
    if not user:
        user = User.objects.create(username=postdata['email'],password=make_password(postdata['password']),email=postdata['email'],first_name=postdata['name'])
        login(request,user)
        return JsonResponse({"user": UserSerializer(user).data}	)
    else:
        return JsonResponse({"message": "Email already Exists."}, status=status.HTTP_400_BAD_REQUEST)
    
# Login API
@csrf_exempt
def signin(request):
    postdata = request.POST
    email = postdata['email']
    password = postdata['password']
    try:
        user = User.objects.get(username=postdata['email'])
    except:
        user = None
    print(user,email,password)
    if user and email and password:
        user = authenticate(username=email, password=password)
        if user:
            login(request,user)
            return JsonResponse({"user": UserSerializer(user).data})
        else:
            return JsonResponse({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
def user_pregnancy_info(request):
    if request.method == "POST":
        weight = request.POST['weight']
        height = request.POST['height']
        weeks_pregnant = request.POST['weeks_pregnant']
        user = request.POST['user_id']
        if weight and height and weeks_pregnant and user:
            models.UserPregnancyInfo.objects.create(user_id=user,weight=weight,height=height,weeks_pregnant=weeks_pregnant)
            return JsonResponse({"message": "User Pregnancy Info Added"})
        else:
            return JsonResponse({"message": "User Pregnancy Info Not Added"})
        
@csrf_exempt
def user_mood(request):
    if request.method == "POST":
        mood = request.POST['mood']
        user = request.POST['user_id']
        if mood and user:
            models.UserMood.objects.create(user_id=user,mood=mood)
            return JsonResponse({"message": "User Mood Added"})
        else:
            return JsonResponse({"message": "User Mood Not Added"})