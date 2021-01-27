from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from cal.middleware import get_request


# class for creating HTML calendar to display tasks 
class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):                              #initialize class with variables year and month
		self.year = year
		self.month = month
        
		super(Calendar, self).__init__()

	
	def formatday(self, day, events):                                       # function formats a day as a td(cell in table) and filters 
		events_per_day = events.filter(task_date__day=day)                  # though days. Returns each day number as html 
		d = ''
		for event in events_per_day:                                        #loop filters to see if there are any tasks and prints link 
			d += f"<li> <h6 id='caldate'>{event.get_html_url}</h6> </li>"                         #if there are 

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"#returns the html cell 
		return '<td></td>'

	
	def formatweek(self, theweek, events):                                #function to format each week as tr(table row)
		week = ''                                                         #assign string to week
		for d, weekday in theweek:                                        #for loop to go through week and format it with the days from 
			week += self.formatday(d, events)                             #above 
		return f"<tr><label id='calweek'> {week}</label> </tr>"                                       #return the row html code 

	def formatmonth(self, withyear=True):                                 #function to format each month at a time

		user_id = get_request().user                                      #define user_id as current user using the custom middleware function: get_request

		# define event varibale used in previous function as filtered object from current user and current month 
		events = Event.objects.filter(username = user_id).filter(completion = 0).filter(task_date__year=self.year, task_date__month=self.month)


		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'     #set bootstrap classes for calendar
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'       #call function to format names 
		cal += f'{self.formatweekheader()}\n'                                              #format weeks 
		for week in self.monthdays2calendar(self.year, self.month):                        #for loop to render the calendar
			cal += f'{self.formatweek(week, events)}\n'
		return cal                                                                         #return the calendar 
 
