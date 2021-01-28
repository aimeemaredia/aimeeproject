#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    utils.py file for creating a calendar object class and defining calendar methods   

#imports
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from cal.middleware import get_request


# class for creating HTML calendar to display tasks 
class Calendar(HTMLCalendar):

	#initialize class with variables year and month
	def __init__(self, year=None, month=None):                             
		self.year = year
		self.month = month
        
		#intialize with the Calendar
		super(Calendar, self).__init__()

	    #function formats a day as a td(cell in table) and filters through days.
	def formatday(self, day, events):            
		#loop filters to see if there are any tasks on the specific day 
		events_per_day = events.filter(task_date__day=day)                  
		d = ''
		#checks all the events and prints out the name as a url if the task it on the specific day 
		for event in events_per_day:                                       
			d += f"<li> <h6 id='caldate'>{event.get_html_url}</h6> </li>"                         

		if day != 0: 
			#Returns each day number as html and returns the html cell 
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>" 
			#returns nothing
		return '<td></td>'

	 #function to format each week as tr(table row)
	def formatweek(self, theweek, events):      
		 #assign string to week                         
		week = ''                              
		#for loop to go through week and format it with the days from above                          
		for d, weekday in theweek:                                        
			week += self.formatday(d, events)         
	    #return the row html code                   
		return f"<tr><label class='date'>{week}</label> </tr>"

    #function to format each month at a time
	def formatmonth(self, withyear=True):  
		#define user_id as current user using the custom middleware function: get_request                              
		user_id = get_request().user                                    

		# define event varibale used in previous function as filtered object from current user and current month 
		events = Event.objects.filter(username = user_id).filter(completion = 0).filter(task_date__year=self.year, task_date__month=self.month)


		cal = f'<table border="1" cellpadding="0" cellspacing="0" class="calendar">\n'     #set bootstrap classes for calendar
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'       #call function to format names 
		cal += f'{self.formatweekheader()}\n'                                              #format weeks 
		for week in self.monthdays2calendar(self.year, self.month):                        #for loop to render the calendar
			cal += f'{self.formatweek(week, events)}\n'
		return cal                                                                         #return the calendar 
 
