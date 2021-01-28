#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    forms.py file settings 

#imports 
from users.models import Profile
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Task 
import datetime
from django.utils import timezone

#object class for task entry 
class TaskForm(forms.ModelForm):
   complete = forms.BooleanField()                               #boolean field to see of task is complete
   task = forms.CharField()                                      #task name with character field 
   type = forms.CharField()                                      #type name with character field
   date = forms.DateField()                                      #date field
   hours_planned = forms.IntegerField()                          #hours planner as integer
   priority = forms.ChoiceField(choices = Task.PRIORITY)         #priority as choice field with 3 choices "low","medium","high"

   class Meta:                                                   #meta class 
       model = Task                                              #model used is Task model
       fields = ['complete','task', 'type', 'date','desc',
                 'hours_planned','hours_worked','priority']      #necessary fields 
