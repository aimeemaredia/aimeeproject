#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    models.py file to create Profile database model 

#imports 
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#Create the model class for profile 
class Profile(models.Model):
    #create user field which will be the current user 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #create image field for profile image 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    #return the profile username as a string 
    def __str__(self):
        return f'{self.user.username} Profile'

