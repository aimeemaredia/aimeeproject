#imports 
from django.urls import path
from . import views 
from .views import TaskDetailView, edittask
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from users.views import profile

# dictionary for url patterns 
urlpatterns = [

    # url path to home screen with task form
    path('home/', views.home, name='planner-home'),       
    # url path to about screen                
    path('about/', views.about, name='planner-about'),
    # url path to dashboard screen
    path('dashboard/', views.dashboard, name='planner-dashboard'),
    # url path to alltasks which displays in the dashboard
    path('all-tasks/',views.alltasks, name="planner-all-tasks"),
    # url path to display high priority tasks
    path('high-tasks/',views.hightasks, name="planner-high-tasks"),
    # url path to display medium priority tasks
    path('medium-tasks/',views.mediumtasks, name="planner-medium-tasks"),
    # url path to display low priority tasks
    path('low-tasks/',views.lowtasks, name="planner-low-tasks"),
    # url path to display tasks with this month
    path('month-tasks/',views.monthtasks, name="planner-month-tasks"),
    # url path to display current task detail 
    path('week-tasks/',views.weektasks, name="planner-week-tasks"),
    # url path to display current task detail 
    path('year-tasks/',views.yeartasks, name="planner-year-tasks"),
    # url path to display current task detail 
    path('complete-tasks/',views.completetasks, name="planner-complete-tasks"),
    # url path to display current task detail 
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    # url path to delete task
    path('delete/<task_id>',views.delete_task,name='delete'),
    # url path to edit task
    path('edit/<task_id>',views.edit_task,name='edit'),
    # url path to complete task
    path('complete/<int:item_id>',views.complete,name='complete'),
    # url path to add task page
    url(r'^add_task/$', views.add_task, name="add_task"),
    path('update_task/', views.edittask, name="update_task"),
    url(r'^edit_task/(?P<task_id>\D+)/$', views.edittask, name='edit_task')
    
]

# loop to add dynamic profile picture to urlpatterns, accessed from the media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)