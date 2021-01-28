#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    admin.py file to register database models 

# import
from planner.models import Task
from django.contrib import admin

# register database Task
admin.site.register(Task)
