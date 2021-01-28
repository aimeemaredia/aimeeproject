#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    views.py file for creating a Calendar view using the calendar class to display the calendar and headers   

#imports
from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar

#class CalendarView (object) to be displayed as a listview instance 
class CalendarView(generic.ListView):

    model = Event                                              #the database used will be Event
    template_name = 'cal/calendar.html'                        #the html template rendered will be calendar.html

    def get_context_data(self, **kwargs):                      #function context data with unbounded parameters (kwargs)

        context = super().get_context_data(**kwargs)           #initialize get_context_data to be accessed anywhere 

        d = get_date(self.request.GET.get('month', None))      #assign date to variable d while leaving out the month

        cal = Calendar(d.year, d.month)                        #call the Calendar function and initialize with parameters date(month) and (year)

        html_cal = cal.formatmonth(withyear=True)              #call function formatmonth from utils.py and initialize with year showing 

        context['calendar'] = mark_safe(html_cal)              #use context for the calendar and assign all strings as safe for output
        context['prev_month'] = prev_month(d)                  #put function prev_month in context to be used later 
        context['next_month'] = next_month(d)                  #put function next_month in context to be used later 
        return context                                         #return the context 

def get_date(req_month):                                       #function to get current date with 1 parameter

    if req_month:                                              
        year, month = (int(x) for x in req_month.split('-'))   #if loop to split current date into 2 strings, month and year 
        return date(year, month, day=1)                        # return the vars month, date and year 
    return datetime.datetime.today()                           # also return today's full date 

def prev_month(d):                                             #function to assign to prev_month button

    first = d.replace(day=1)                                   #assign day var to first var
    prev_month = first - timedelta(days=1)                     #assign prev_month as time between the days minus first var
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month) #assign month var as string include previous month and previous year
    return month                                               #return the previous month 

def next_month(d):                                             #function to assign to next_month button 
    
    days_in_month = calendar.monthrange(d.year, d.month)[1]    #call method to find days in current month 
    last = d.replace(day=days_in_month)                        #assign var with days from the month 
    next_month = last + timedelta(days=1)                      #add the change in days to the days this month to get days next month
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)#assign month and year string to var month 
    return month                                               #return the next month