#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    views.py file all the methods and views that will be rendering in html template

#imports 
from django.contrib.auth import login
from django.http import request
from django.http.response import HttpResponseRedirect
from . models import Task
from cal.models import Event
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from datetime import date
from django.db.models import Sum

# setting local variables 
this_month = timezone.now().month  #setting current month 
this_year = timezone.now().year    #setting current year

# method for enter route
def enter(request):
    return render(request, 'planner/enter.html')


# home function 
@login_required
def home(request): 
    # context vars to be used when called
    context = {
        #dictionary, filter all tasks and us those with current user id 
        'tasks': Task.objects.filter(user_written=request.user).filter(complete=0).all()
    }

    #return and render task_form.html and context vars
    return render(request, 'planner/task_form.html', context)
    
#object class navTasks for list view
class navTasks(ListView):
    model = Task                                 #use model Task
    template_name = 'planner/dashboard.html'     # load dashboard.html
    context_object_name = 'tasks'                #use context 'tasks'
  

#object class detail view to display selected task
class TaskDetailView(DetailView):
    model = Task                                  #use model task 

#object class to create task
class createtask(CreateView):

    model = Task                                  #use model Task
    context_object_name ='tasks'                  #use context 'tasks'
    fields =['task','type','date','hours_planned','desc','priority'] #form fields from task model to be displayed
    template_name = 'planner/base.html'           #return base.html

#function to call the about page 
def about (request): 
    #return about.html
    return render(request, 'planner/about.html', {'title': 'About'})



#function to get data from the form and save to database
@login_required
def add_task(request):
    
    #print for debugging 
    print("form is submitted")
    
    # save form input fields as local variables using POST django method 
    task = request.POST["task"]                    #save task field 
    date = request.POST["date"]                    #save date field 
    task_date = request.POST["date"]               #save date field for alternate use 
    hours_planned = request.POST["hours_planned"]  #save hours planned
    correctdate=None                               #set correctdate boolean as none
    type = request.POST["type"]                    #save type field 
    desc = request.POST["desc"]                    #save description field 
    priority = request.POST['priority']            #save priority field 
    title = request.POST["task"]                   #save task as title for alternate use 
    
     # check to see if hours field is filled
    try: 
        #check to see if the hours are a int
        int(hours_planned) == int
        correctdate=True
    #do next loop if not an int
    except ValueError:
        # set default hours to one 
        hours_planned = 1 
        correctdate=False
   
    # try and except loop to check if datefield is filled
   
    try:
        #try to parse the input date 
        getdate = datetime.datetime.strptime(str(date),"%Y-%m-%d")   
        #try to get individual fields from the date 
        newdate = datetime.datetime(getdate.year,getdate.month,getdate.day)
        
    #if the above commands throw an error then move to except loop
    except ValueError:
        #set date to current date as default 
        date = datetime.date.today() 
        #set task_date to current date 
        task_date = datetime.date.today()

   

    #set date to mystring 
    my_string = date    
    #parse mystring to split the date into 3 different strings for day, month, and year                                     
    my_date = datetime.datetime.strptime(str(my_string),"%Y-%m-%d")
    #use the newly created strings to find the week posted using the strftime method 
    date_added_week = datetime.date(my_date.year, my_date.month, my_date.day).strftime('%V')
    #save current user as user_written 
    user_written = request.user
    #use the previously declared local variables and assign them to fields in the Task database 
    add_task = Task(task=task, date=date, type=type, desc=desc, hours_planned=hours_planned, priority=priority, date_added_year = my_date.year, date_added_month = my_date.month, date_added_day = my_date.day, date_added_week=date_added_week, user_written=user_written )
    #save the Task model 
    add_task.save()
    #use the previously declared local variables and assign them to fields in the Event database 
    cal_update = Event(title=title, task_date=task_date)
    #save the Event model
    cal_update.save()
    #define the context 
    context = {
        #all tasks object entered by current user and are not completed 
        'tasks': Task.objects.filter(user_written = request.user).filter(complete=0).all()
    }

    #Task count for debugging purposes 
    obj = Task.objects.count()
    print(""+ str(obj)) 
    #return the task_form html template if the method is successful, also return the context variables 
    return render(request, 'planner/task_form.html', context)

def edittask(request):
    
    #print for debugging 
    print("form is submitted")
    
    #define local variables from input using POST method 
    task = request.POST["task"]                     #save task field 
    date = request.POST["date"]                     #save date field
    task_date = request.POST["date"]                #save date field
    hours_planned = request.POST["hours_planned"]   #save hours planned
    task_id = request.POST["hidden"]                #save task id 
    type = request.POST["type"]                     #save type field 
    desc = request.POST["desc"]                     #save description field
    priority = request.POST['priority']             #save priority field 
    title = request.POST["task"]                    #save title field 
    correctdate=None                                #set correctfield boolean to None 
    
    # try and except loop to check if datefield is filled
    try:
        #try to parse the input date 
        getdate = datetime.datetime.strptime(str(date),"%Y-%m-%d")   
        #try to get individual fields from the date 
        newdate = datetime.datetime(getdate.year,getdate.month,getdate.day)
       
    #if the above commands throw an error then move to except loop
    except ValueError:
        #set date to current date as default 
        date = datetime.date.today() 
        #set task_date to current date 
        task_date = datetime.date.today()

    # check to see if hours field is filled
    try: 
        #check to see if the hours are a int
        int(hours_planned) == int
    #do next loop if not an int
    except ValueError:
        # set default hours to one 
        hours_planned = 1 
        
    #set date to mystring 
    my_string = date    
    #parse mystring to split the date into 3 different strings for day, month, and year                                     
    my_date = datetime.datetime.strptime(str(my_string),"%Y-%m-%d")
    #use the newly created strings to find the week posted using the strftime method 
    date_added_week = datetime.date(my_date.year, my_date.month, my_date.day).strftime('%V')
    #save current user as user_written 
    user_written = request.user
    #update the current chosen task in the Task model using local variables defined above 
    Task.objects.filter(id=task_id).update(task=task, date=date, type=type, desc=desc, hours_planned=hours_planned, priority=priority, date_added_year = my_date.year, date_added_month = my_date.month, date_added_day = my_date.day, date_added_week=date_added_week, user_written=user_written )
    #update the current chosen task in the Event model using local variables defined above 
    Event.objects.filter(id=task_id).update(title=title, task_date=task_date)
   
    # print for debugging purposes
    obj = Task.objects.count()
    print(""+ str(obj)) 
    # return the home page of the program 
    return redirect('planner-home')

#method to delete the chosen tasks, task id as a parameter 
def delete_task(request, task_id = None):
    #get the task using the chosen task id 
    post_to_delete=Task.objects.get(id=task_id)
    #delete the chosen task 
    post_to_delete.delete()
    #get the event using the task id
    event_to_delete = Event.objects.get(id=task_id)
    #delete the chosen event 
    event_to_delete.delete()
    #redirect the user to the home page 
    return redirect('planner-home')

#method to complete a task 
def edit_task(request, task_id = None):

    context = {
    'tasks': Task.objects.filter(id = task_id).all()                                                
    }                              
    return render(request,'planner/editform.html',context)

#method to complete a task, item id as a parameter to choose the task 
def complete(request,item_id = None):
    #filter through the database using task id and change the complete boolean to true
    Event.objects.filter(id=item_id).update(completion = True)
    #filter through the database using task id and change the completion boolean to true
    Task.objects.filter(id=item_id).update(complete=True)
    #redirect to home page 
    return redirect(request.META['HTTP_REFERER'])
           
def help(request):
    
    return render(request, 'planner/help.html')

#function to call dashboard page and define context variables 
@login_required        #decorator to require login
def dashboard (request): 
    my_date = datetime.date.today()                    #save today's date in local variable           
    this_week = "0"+ str(my_date.isocalendar()[1])     #save today's week as iso number in local variable 
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00) 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00) 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)   
        # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        #filter to assign totalhours var to totalhours
        'totalhours': totalhours,
        #filter from current user and uncompleted tasks for total tasks
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),  
        #filter from current user and uncompleted tasks for high priority tasks                                
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),  
        #filter from current user and uncompleted tasks for medium priority tasks              
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        #filter from current user and uncompleted tasks for low priority tasks          
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),  
        #filter from current user and uncompleted tasks for tasks this week                 
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        #filter from current user and uncompleted tasks for tasks this month 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()),   
        #filter from current user and uncompleted tasks for tasks this year  
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()), 
        #filter from current user and uncompleted tasks for completed tasks
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count())    
       
    }
    #return dashboard.html
    return render(request, 'planner/dashboard.html', context)

#method to set context variables when user wants to diplay all tasks 
@login_required
def alltasks(request): 
    #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    print(totalhours)
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {

        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),  
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),                
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),  
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).all(), 
        #filter from current user for completed tasks       
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count())                                               
    }
    #return the all tasks Html templates 
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display high prioriy tasks
@login_required
def hightasks(request): 
   #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),    
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),  
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),     
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for high priority tasks 
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').all()
            
    }
    #return alltasks.html page 
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display medium prioriy tasks
@login_required
def mediumtasks(request): 
   #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),       
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),     
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),  
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for medium priority tasks
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').all()
                  
    }
    #return alltasks.html page 
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display low prioriy tasks
@login_required
def lowtasks(request): 
  #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),  
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),  
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()), 
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for low priority tasks   
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').all(),
    }
    # return alltasks.html page
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display tasks this month
@login_required
def monthtasks(request): 
    #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),   
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()), 
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for the month 
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).all()
                      

    }
    #return the alltasks.html template 
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display tasks this week
@login_required
def weektasks(request): 
    #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
     # check and set var if lower than 0
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),   
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),  
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for the week to show all
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week = this_week).all()
        
    }
    # return alltasks.html page
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display tasks today
@login_required
def daytasks(request): 
    #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),   
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),  
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for the week to show all
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day = this_day).all()
        
    }
    # return alltasks.html page
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display tasks this year
@login_required
def yeartasks(request): 
    #set current year 
    this_year = "2021"
    #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()), 
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),  
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()), 
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),  
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user and uncompleted tasks for the year to show all
        'items': Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year = this_year).all(),        

    }
    # return alltasks.html page 
    return render(request, 'planner/alltasks.html', context)

#method to set context variable when user wants to display completed tasks
@login_required
def completetasks(request): 
    #set current date
    my_date = datetime.date.today() 
    #set current week as string 
    this_week = "0"+ str(my_date.isocalendar()[1])
    this_day = timezone.now().day
    #filter through database for hours planned and sort for total, this day, week and month and save as local variable
    totalhours = int(Task.objects.filter(user_written = request.user).filter(complete=0).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00))  #filter through database for total hours planned and save as local variable 
    hourmonth = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourweek = Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00)  #filter through database for total hours planned and save as local variable 
    hourday = int(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).aggregate(Sum('hours_planned')).get('hours_planned__sum',0.00))  #filter through database for total hours planned and save as local variable 
    # check and set var if lower than 1
    if totalhours is None: totalhours = 0
    if hourmonth is None: hourmonth = 0
    if hourweek is None: hourweek = 0
    if hourday is None: hourday = 0
    #define context variables
    context = {
        'totalhours': totalhours,
        'total' : str(Task.objects.filter(user_written = request.user).filter(complete=0).all().count()),      
        'high' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='High').count()),     
        'medium' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Medium').count()),  
        'low' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(priority='Low').count()),
        'day' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_day=this_day).count()),
        'hourmonth': hourmonth,
        'hourweek' : hourweek,
        'hourday' : hourday,
        'week' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_week=this_week).count()), 
        'month' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_month=this_month).count()),
        'year' : str(Task.objects.filter(user_written = request.user).filter(complete=0).filter(date_added_year=this_year).count()),    
        'complete' : str(Task.objects.filter(user_written = request.user).filter(complete = 1).count()),  
        #filter from current user for completed tasks and show all
        'items': Task.objects.filter(user_written = request.user).filter(complete=1).all(),                       

    }
    # return alltasks.html page 
    return render(request, 'planner/alltasks.html', context)





