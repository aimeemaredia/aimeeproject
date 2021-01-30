#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    models.py file for the Task database model

#imports
from django.db import models
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, NullBooleanField
from django.forms.fields import BooleanField
from django.utils import timezone
from django.contrib.auth.models import User 
import datetime
from users.models import Profile
from django.urls import reverse
import datetime


#object class model Task to store task variables 
class Task(models.Model):

    complete = models.BooleanField(default='False')                                       #complete as boolean, set default to false
    task = models.CharField(max_length=200)                                               #task as character field
    date_added = models.DateField(default= timezone.now)                                  #date added as date time field
    date_added_year = models.CharField(max_length=4,default="0000")                       #date added year as character field
    date_added_month = models.CharField(max_length=2, default="00")                       #date added month as character field
    date_added_day = models.CharField(max_length=2, default="00")                         #date added day as character field
    date_added_week = models.CharField(max_length=2, default="00")                        #date added week as character field
    type = models.CharField(max_length=200)                                               #type as character field
    date = models.DateField(default = datetime.date.today, editable = True, blank = True) #due date as datefield, set default to now 
    desc = models.TextField(max_length=500, default= "enter")                             #description as textfield 
    hours_planned = models.IntegerField(default=0)                                        #hours planned as int
    hours_worked = models.IntegerField(default=0)                                         #hours worked as int
    priority = models.CharField(max_length=32)                                            #priority as charfield
    user_written = models.ForeignKey(User, default=1, verbose_name='user', on_delete=models.CASCADE) #set foreign key to User to sort through user tasks

        #define property of model Event
    @property
    def get_html_url(self):                               #function to return link
        url = reverse('task-detail', args=(self.id,))     #redirct user to task detail view, corresponding to task id 
        return f'<a id ="calLink" href="{url}"> {self.task}</a>'       #return the link on form of html code with title 