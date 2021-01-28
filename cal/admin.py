#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    admin.py file for registering database models  

#imports 
from django.contrib import admin
from cal.models import Event 

# register Event database model 
admin.site.register(Event)