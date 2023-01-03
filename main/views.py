from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request,template_name="main/home.html"):
    return render(request,template_name)

def login(request):
    return JsonResponse({"hey":"hi"})