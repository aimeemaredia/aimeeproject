# #imports 
# from django.contrib.auth import login
# from django.http import request
# from . models import Task
# from cal.models import Event
# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# import datetime
# from datetime import date
# from django.db.models import Sum


# this_month = timezone.now().month
# this_year = timezone.now().year

# entries = {
# 'total' : str(Task.objects.all().count()),
# 'high' : str(Task.objects.filter(priority='high').count()),
# 'medium' : str(Task.objects.filter(priority='medium').count()),
# 'low' : str(Task.objects.filter(priority='low').count()),
# 'month' : str(Task.objects.filter(date_added_month=this_month).count()),
# 'year' : str(Task.objects.filter(date_added_year=this_year).count())

# }
# def enter(request):
#     return render(request, 'planner/enter.html')


# # home function 
# @login_required
# def home(request): 
#     # context vars to be used when called
#     context = {
#         #dictionary, filter all tasks and us those with current user id 
#         'tasks': Task.objects.filter(user_written=request.user).filter(complete=0).all()
#     }

#     #return and render task_form.html and context vars
#     return render(request, 'planner/task_form.html', context)
    
# #object class navTasks for list view
# class navTasks(ListView):
#     model = Task                                 #use model Task
#     template_name = 'planner/dashboard.html'     # load dashboard.html
#     context_object_name = 'tasks'                #use context 'tasks'
  

# #object class detail view to display selected task
# class TaskDetailView(DetailView):
#     model = Task                                  #use model task 

# #object class to create task
# class createtask(CreateView):

#     model = Task                                  #use model Task
#     context_object_name ='tasks'                  #use context 'tasks'
#     fields =['task','type','date','hours_planned','desc','priority'] #form fields from task model to be displayed
#     template_name = 'planner/base.html'           #return base.html

# #function to call the about page 
# def about (request): 
#     #return about.html
#     return render(request, 'planner/about.html', {'title': 'About'})

# #function to call dashboard page and define context variables 
# @login_required
# def dashboard (request): 
#     my_date = datetime.date.today()
#     this_week = "0"+ str(my_date.isocalendar()[1])
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()), 
#         'totalhours': str(Task.objects.filter(user_written = request.user).aggregate(Sum('hours_planned'))),
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),       #filter from current user for tasks this year
       
#     }
#     print(''+str(Task.objects.all().count()))
#     print(''+str(this_week))
#     #return dashboard.html
#     return render(request, 'planner/dashboard.html', context)

# #function to get data from the form and save to database
# @login_required
# def add_task(request):
    
#     my_user = request.user 
#     print("form is submitted")
    
#     task = request.POST["task"]
#     date = request.POST["date"]
#     task_date = request.POST["date"]
#     hours_planned = request.POST["hours_planned"]
    
#     correctdate=None
    
#     try:
#         getdate = datetime.datetime.strptime(str(date),"%Y-%m-%d")
#         newdate = datetime.datetime(getdate.year,getdate.month,getdate.day)
#         hours_planned == int
#         correctdate=True
#         print("true")
#     except ValueError:
#         date = datetime.date.today() 
#         task_date = datetime.date.today()
#         hours_planned = 1 
#         correctdate=False
#         print("false")

        
    
#     my_string = date                                        
#     my_date = datetime.datetime.strptime(str(my_string),"%Y-%m-%d")
#     type = request.POST["type"]
#     desc = request.POST["desc"]
    
#     priority = request.POST['priority']
#     date_added_week = datetime.date(my_date.year, my_date.month, my_date.day).strftime('%V')
#     user_written = request.user
#     title = request.POST["task"]
    
#     add_task = Task(task=task, date=date, type=type, desc=desc, hours_planned=hours_planned, priority=priority, date_added_year = my_date.year, date_added_month = my_date.month, date_added_day = my_date.day, date_added_week=date_added_week, user_written=user_written )
#     add_task.save()
#     cal_update = Event(title=title, task_date=task_date)
#     cal_update.save()
#     context = {
    
#         'tasks': Task.objects.filter(user_written = request.user).all()
#     }
#     obj = Task.objects.count()
#     print(""+ str(obj)) 
#     return render(request, 'planner/task_form.html', context)

# def edittask(request):
#     my_user = request.user 
#     print("form is submitted")
    
#     task = request.POST["task"]
#     date = request.POST["date"]
#     task_date = request.POST["date"]
#     hours_planned = request.POST["hours_planned"]
#     task_id = request.POST["hidden"]
#     correctdate=None
    
#     try:
#         getdate = datetime.datetime.strptime(str(date),"%Y-%m-%d")
#         newdate = datetime.datetime(getdate.year,getdate.month,getdate.day)
#         hours_planned == int
#         correctdate=True
#         print("true")
#     except ValueError:
#         date = datetime.date.today() 
#         task_date = datetime.date.today()
#         hours_planned = 1 
#         correctdate=False
#         print("false")

        
    
#     my_string = date                                        
#     my_date = datetime.datetime.strptime(str(my_string),"%Y-%m-%d")
#     type = request.POST["type"]
#     desc = request.POST["desc"]
    
#     priority = request.POST['priority']
#     date_added_week = datetime.date(my_date.year, my_date.month, my_date.day).strftime('%V')
#     user_written = request.user
#     title = request.POST["task"]
    
#     update_task = Task.objects.filter(id=task_id).update(task=task, date=date, type=type, desc=desc, hours_planned=hours_planned, priority=priority, date_added_year = my_date.year, date_added_month = my_date.month, date_added_day = my_date.day, date_added_week=date_added_week, user_written=user_written )
#     cal_update = Event.objects.filter(id=task_id).update(title=title, task_date=task_date)
   
#     context = {
    
#         'tasks': Task.objects.filter(id=task_id).all()
#     }
#     obj = Task.objects.count()
#     print(""+ str(obj)) 
#     return render(request, 'planner/editform.html', context)


# def delete_task(request, task_id = None):
#     post_to_delete=Task.objects.get(id=task_id)
#     post_to_delete.delete()
#     event_to_delete = Event.objects.get(id=task_id)
#     event_to_delete.delete()
#     return redirect('planner-home')

# def edit_task(request, task_id = None):

#     context = {
#     'tasks': Task.objects.filter(id = task_id).all()                                                
#     }                              
#     return render(request,'planner/editform.html',context)

# def complete(request,item_id = None):
#     Event.objects.filter(id=item_id).update(completion = True)
#     Task.objects.filter(id=item_id).update(complete=True)
#     return redirect('planner-home')
           

# @login_required
# def alltasks(request): 
 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()), 
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).all()                                                      
#     }
#     return render(request, 'planner/alltasks.html', context)

# @login_required
# def hightasks(request): 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()), 
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).filter(priority='high').all()                         #filter from current user for high priority tasks
#     }
#     return render(request, 'planner/alltasks.html', context)

# @login_required
# def mediumtasks(request): 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()), 
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).filter(priority='medium').all()                         #filter from current user for high priority tasks
#     }
#     return render(request, 'planner/alltasks.html', context)

# @login_required
# def lowtasks(request): 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()), 
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).filter(priority='low').all()                         #filter from current user for high priority tasks
#     }
#     return render(request, 'planner/alltasks.html', context)

# @login_required
# def monthtasks(request): 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()), 
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).all()                         #filter from current user for high priority tasks

#     }
#     return render(request, 'planner/alltasks.html', context)

# @login_required
# def weektasks(request): 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),  
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).filter(date_added_week = this_week).all()                         #filter from current user for high priority tasks

#     }
#     return render(request, 'planner/alltasks.html', context)

# @login_required
# def yeartasks(request): 
#     my_date = datetime.date.today()
#     this_week = my_date.isocalendar()
#     this_year = "2021"
#     context = {
#         'total' : str(Task.objects.filter(user_written = request.user).all().count()),                                  #filter from current user for total tasks
#         'high' : str(Task.objects.filter(user_written = request.user).filter(priority='high').count()),                 #filter from current user for high priority tasks
#         'medium' : str(Task.objects.filter(user_written = request.user).filter(priority='medium').count()),             #filter from current user for medium priority tasks
#         'low' : str(Task.objects.filter(user_written = request.user).filter(priority='low').count()),                   #filter from current user for low priority tasks
#         'month' : str(Task.objects.filter(user_written = request.user).filter(date_added_month=this_month).count()),    #filter from current user for tasks this month
#         'year' : str(Task.objects.filter(user_written = request.user).filter(date_added_year=this_year).count()),  
#         'week' : str(Task.objects.filter(user_written = request.user).filter(date_added_week=this_week).count()),       #filter from current user for tasks this year
#         'items': Task.objects.filter(user_written = request.user).filter(date_added_year = this_year).all()                         #filter from current user for high priority tasks

#     }
#     return render(request, 'planner/alltasks.html', context)


# def createtask(request):
     
#        if request.method == 'TASK':
#            if request.TASK.get('task') and request.TASK.get('date') and request.TASK.get('type') and request.TASK.get('desc'):
#                task= Task()
#                task.task= request.TASK.get('task')
#                task.type= request.TASK.get('type')
#                task.date= request.TASK.get('date')
#                task.save()
               
#                return render(request, 'tasks/create.html')  

#        else:
#                return render(request,'tasks/create.html')

# # def CreateTask(request):
# #    if request.method == 'POST':
# #        t_form = TaskForm(request.POST)
# #        if t_form.is_valid():
# #            t_form.save()
# #            return redirect('planner-home')
# #    else:
# #        t_form = TaskForm()
# #    return render(request, 'planner/home.html', {'form': t_form})

