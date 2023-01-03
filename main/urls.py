from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_template,name="login"),
    path('register/',views.register_template,name="login"),
    path('api/signin/',views.login_api,name="signin"),
    path('api/signup/',views.register_api,name="signup")
]
