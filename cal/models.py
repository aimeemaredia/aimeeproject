from django.db import models
import datetime
from django.contrib.auth.models import User 
from django.urls.base import reverse

# Event model to store necessary field for the calendar 
class Event(models.Model):
    title = models.CharField(max_length=200)                                                      #title is the name of the task (chars)
    description = models.TextField()                                                              #description of the tast (text)
    task_date = models.DateField()                                                                #task due date (datefield)
    priority = models.CharField(max_length=32, default='low')                                     #priority of the task 
    completion = models.BooleanField(default='False')                                             #completion boolean 
    username = models.ForeignKey(User, default=1, verbose_name='user', on_delete=models.CASCADE)  #foreign key to attach to User db and sort by user

    #define property of model Event
    @property
    def get_html_url(self):                               #function to return link
        url = reverse('task-detail', args=(self.id,))     #redirct user to task detail view, corresponding to task id 
        return f'<a href="{url}"> {self.title}</a>'       #return the link on form of html code with title 