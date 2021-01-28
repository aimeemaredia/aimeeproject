#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    urls.py file for routing url routes in the calendar app 

#imports 
from django.conf.urls import url
from . import views
from django.urls import path
from planner.views import TaskDetailView

# register app name
app_name = 'cal'

# url mapping patterns 
urlpatterns = [ 
    #calendar url will return calendar page 
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),      
]