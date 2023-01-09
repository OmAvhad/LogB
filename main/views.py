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

@csrf_protect
# @csrf_exempt
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

@csrf_protect
# @csrf_exempt
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