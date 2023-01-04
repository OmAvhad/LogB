from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Blogs
from django.http import JsonResponse
from main.views import Response
from django.contrib.auth.models import User
from .operations import validateBlogCreation, serializeBlogs, userExsits
# Create your views here.


# create blog
# publish blog
# list blogs
@csrf_exempt
def getBlogs(request):
    if request.method == "GET":
        blogs = Blogs.objects.all()
        if blogs.count() > 0:
            data = serializeBlogs(blogs)
            status='succesfull'
            status_code=200
        else:
            status='failed'
            status_code=400
        return JsonResponse(Response(status=status,status_code=status_code,data=data))


@csrf_exempt
def getMyBlogs(request):
    status='failed'
    status_code=400
    data = []
    message = ''
    if request.method == "POST":
        postdata = request.POST
        if "author_id" in postdata:
            if userExsits(postdata['author_id']):
                blogs = Blogs.objects.filter(author_id=postdata['author_id'])
                if blogs.count() > 0:
                    data = serializeBlogs(blogs)
                    status = 'succesfull'
                    status_code = 200
                    message = "Blogs Feteched Successfully"
            else:
                message = "User not found"   
        else:
            message = "Send required details"     
    return JsonResponse(Response(status=status,status_code=status_code,message=message,data=data))
    
    
@csrf_exempt
def createBlog(request):
    status = "failed"
    status_code = 400
    if request.method == "POST":
        val = validateBlogCreation(request.POST)
        if val['bool']:
            postdata = request.POST
            if userExsits(postdata['author_id']):
                Blogs.objects.create(title=postdata['title'],author_id=postdata['author_id'],content=postdata['content'])
                status = "successfull"
                status_code = 200
                message = "Blog created Successfully"
            else:
                message = "User not found"
        else:
            message = val['message']
        return JsonResponse(Response(status=status,status_code=status_code,message=message))