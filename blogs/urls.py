from django.urls import path
from . import views
app_name = "blogs"

urlpatterns = [
    path('create/blog',views.create_blog_template,name="create_blog_template"),
    path('myblogs',views.myblogs_template,name="myblogs_template"),
    
    path('api/get/blogs/',views.getBlogs,name="get_blogs"),
    path('api/create/blog/',views.createBlog,name="create_blog"),
    path('api/publish/blog/',views.publishBlog,name="get_my_blogs"),
    path('api/get/myblogs/',views.getMyBlogs,name="get_my_blogs"),
    path('api/get/categories/',views.getAllCategories,name="get_all_categories")
]