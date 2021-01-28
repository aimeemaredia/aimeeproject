#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    signals.py file to use signal to automatically create
#    a profile when a new user is created 


#imports 
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import User

#receiver to get a signal when a new user is created
@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs): #method to build profile, using instance and created as parameters
  #if a new profile is created:
  if created:
    profile = Profile(user=instance) #create a new instance of the profile 
    profile.save()                   #save the profile 
    