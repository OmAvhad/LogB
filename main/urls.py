from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about_template,name="about"),
    path('login/',views.login_template,name="login"),
    path('register/',views.register_template,name="register"),
    
    path('api/signin/',views.login_api,name="signin"),
    path('api/signup/',views.register_api,name="signup")
]
