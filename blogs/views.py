from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Blogs, Categories, Comments, Likes
from django.http import JsonResponse
from django.contrib.auth.models import User
from .operations import validateBlogCreation, serializeBlogs, userExists, blogExists, serializeCategories
from datetime import datetime
from .serializers import BlogsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def create_blog_template(request,template_name="blogs/write_blog.html"):
    return render(request,template_name)

def myblogs_template(request,template_name="blogs/myblogs.html"):
    return render(request,template_name)

@csrf_exempt
@api_view(['GET'])
def getBlogs(request):
    blogs = Blogs.objects.all().order_by('-id')
    response = BlogsSerializer(blogs, many=True)
    return Response({"message": "Blogs Fetched Successfully", "data":response.data},status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def getMyBlogs(request):
    postdata = request.POST
    if "author_id" in postdata:
        if userExists(postdata['author_id']):
            blogs = Blogs.objects.filter(author_id=postdata['author_id'])
            if blogs.count() > 0:
                response = BlogsSerializer(blogs, many=True)
                status_code = status.HTTP_200_OK
                message = "Blogs Feteched Successfully"
        else:
            status_code = status.HTTP_404_NOT_FOUND
            message = "User not found"   
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Send required details"     
    return Response({"message": message, "data":response.data},status=status_code)
    
    
@csrf_exempt
@api_view(['POST'])
def createBlog(request):
    postdata = request.POST
    if userExists(postdata['author']):
        serialzer = BlogsSerializer(data=postdata)
        if serialzer.is_valid():
            serialzer.save()
            status_code = status.HTTP_201_CREATED
            message = "Blog created Successfully"
        else:
            print(serialzer.errors)
    else:
        status_code = status.HTTP_401_UNAUTHORIZED
        message = "User not found"
    return Response({"message": message},status=status_code)
    

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
    
    
def getCategoryBlogs(request):
    if request.method == "POST":
        postdata = request.POST
        if "cat_id" in postdata:
            blogs = Blogs.objects.filter(category_id =postdata["cat_id"])
            if blogs.count() > 0:
                data = serializeBlogs(blogs)
                status = 'successful'
                status_code = 200
                message = "Blogs found successfully."
            else:
                status = 'successful'
                status_code = 200
                message = "No blogs posted under this category."
        else:
            status = 'failed'
            status_code = 400
            message = "Send required details"
        return JsonResponse(Response(status=status,status_code=status_code,data=data,message=message))