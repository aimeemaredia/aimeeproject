"""FinalProject URL Configuration
"""
#FinalProject URL Configuration
from FinalProject.settings import LOGIN_REDIRECT_URL
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect 
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    #url path to admininistration backpage 
    path('admin/', admin.site.urls),
    #url path to load login page when users first come in
    path('', auth_views.LoginView.as_view(template_name='users/loginfirst.html'), name="login"),
    #url path to the register new user page 
    path('register/', user_views.register, name='register'),
    #url path to the view profile page 
    path('profile/', user_views.profile, name='profile'),
    #url path to the logout screen 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    # redirect to include urls located in the planner folder
    path('', include('planner.urls')),
    # redirect to include urls located in the calendar folder 
    path('', include('cal.urls'))
    
]
