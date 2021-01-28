#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    forms.py file to create the user registration form, the user update form, and profile update form 

#imports 
from users.models import Profile
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 

#user registration form class to create a new user 
class UserRegisterForm(UserCreationForm):
    #set email as an email field 
    email = forms.EmailField()

    #class meta for database association 
    class Meta: 
        #set model to user 
        model = User
        #set field names to username, email and passwork (twice for verification)
        fields = ['username','email', 'password1', 'password2'] 

#user registration form class to update current user information
class UserUpdateForm(forms.ModelForm):
    #set email as an email field 
    email = forms.EmailField()

    #class meta for database association 
    class Meta: 
        #set model to user 
        model = User
        #set field names to username and email
        fields = ['username','email'] 

#user registration form class to update profile information 
class ProfileUpdateForm(forms.ModelForm):

    #class meta for database association 
    class Meta:
        #set model to user 
        model = Profile
        #set fields to image 
        fields = ['image']