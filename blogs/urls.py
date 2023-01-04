from django.urls import path
from . import views
app_name = "blogs"

urlpatterns = [
    path('api/get/blogs/',views.getBlogs,name="get_blogs"),
    path('api/create/blog/',views.createBlog,name="create_blog"),
    path('api/publish/blog/',views.publishBlog,name="get_my_blogs"),
    path('api/get/myblogs/',views.getMyBlogs,name="get_my_blogs"),
]