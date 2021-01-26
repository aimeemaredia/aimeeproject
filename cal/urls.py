#imports 
from django.conf.urls import url
from . import views
from django.urls import path
from planner.views import TaskDetailView

# register app name
app_name = 'cal'

# url mapping patterns 
urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),       #calendar url will return calendar page 
]