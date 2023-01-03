from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request,template_name="main/home.html"):
    return render(request,template_name)

@csrf_protect
def login_api(request):
    if request.method == "POST":
        postdata = request.POST
        username = postdata['username']
        password = postdata['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            status = 'successful'
            status_code = '200'
            message = 'User found'
        else:
            status = 'failed'
            status_code = '400'
            message = 'User not found'
    return JsonResponse(Response(status=status,status_code=status_code,message=message))

# @csrf_protect
def register_api(request):
    if request.method == "POST":
        postdata = request.POST
        try:
            username = postdata['username']
            password = postdata['password']
            first_name = postdata['first_name']
            last_name = postdata['last_name']
            email = postdata['email']
            User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            status = 'successful'
            status_code = '200'
            message = 'User Registered Successfully'
        except:
            status = 'failed'
            status_code = '400'
            message = 'Send all required details.'
        
    return JsonResponse(status=status,status_code=status_code,message=message)

def Response(status,status_code,data={},message = "",):
    response = {'status':status,'status_code':status_code,'data':data,'message':message}
    return response