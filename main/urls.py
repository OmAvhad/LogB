from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin/',views.login_api,name="signin"),
    path('signup/',views.register_api,name="signup")
]
