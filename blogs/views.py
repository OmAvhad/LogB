from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Blogs, Categories, Comments, Likes
from django.http import JsonResponse
from main.views import Response
from django.contrib.auth.models import User
from .operations import validateBlogCreation, serializeBlogs, userExists, blogExists, serializeCategories
from datetime import datetime
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
            if userExists(postdata['author_id']):
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
            if userExists(postdata['author_id']):
                Blogs.objects.create(title=postdata['title'],author_id=postdata['author_id'],content=postdata['content'])
                status = "successfull"
                status_code = 200
                message = "Blog created Successfully"
            else:
                message = "User not found"
        else:
            message = val['message']
        return JsonResponse(Response(status=status,status_code=status_code,message=message))
    

@csrf_exempt
def publishBlog(request):
    status = "failed"
    status_code = 400
    message = ""
    if request.method == "POST":
        postdata = request.POST
        if "author_id" and "blog_id" in postdata:
            if userExists(postdata["author_id"]) and blogExists(postdata["blog_id"]):
                Blogs.objects.filter(id=postdata["blog_id"]).update(is_published=True,published_at=datetime.now())
                status = "success"
                status_code = 200
                message = "Blog Published Successfully" 
            else:
                message = "User or Blog doesnot exists"
        else:
            message = "Send required details"
    return JsonResponse(Response(status=status,status_code=status_code,message=message))


@csrf_exempt
def getAllCategories(request):
    if request.method == "GET":
        cat = Categories.objects.all()
        data = serializeCategories(cat)
        return JsonResponse(Response(status="success",status_code=200,data=data))