# Final Project - Taskable 

## Structure

    - Cal
        - static 
            - styles.css          
        - templates
            - base.html 
            - calendar.html
        - __init__.py
        - admin.py
        - apps.py
        - middleware.py
        - models.py
        - tests.py 
        - urls.py 
        - utils.py 
        - views.py 

    - FinalProject
        - __init__.py
        - asgi.py
        - settings.py 
        - urls.py 
        - wsgi.py

    - media 
        - profile pics

    - planner 
        - static 
            - main.css
            - main.js
        - templates
            - help.html
            - alltasks.html
            - base.html 
            - dashboard.html
            - editform.html
            - enter.html
            - footer.html
            - header.html
            - home.html
            - task_detail.html
            - task_form.html
            - topnav.html          
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - tests.py 
        - urls.py  
        - views.py

    - staticfiles 

    - users  
        - templates
            - login.html
            - loginfirst.html
            - logout.html
            - profile.html 
            - register.html
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - signals.py
        - tests.py  
        - views.py

    - manage.py 

___

### Cal Module

This is the folder that contains all the models, methods and object classes to create the calendar for the program. The module also contains the static CSS formatting files and the HTML templates neccessary to display the page.

#### **Static Folder**

This folder contains the `styles.css` file which contains the formatting for the calendar table (headers, titles, rows and cells).

#### **Template Folder**

This folder contains the HTML template for the calendar. It containts the `base.html` and `calendar.html` files. The base file inherits its javascript headers and footers from the html files located in the planner module. The calendar file renders the calendar view and places it in the base template.

#### **`__init__.py`**

Empty file which is required within the framework to initialize the cal module.

#### **`admin.py`**

Admin file registers the Event database model for use.

#### **`apps.py`**

Apps file initializes the cal module to be able to run the program and reference it from other files

#### **`middleware.py`**

The middleware file creates custom middleware to make the request and response object available globally. The method returned is the `get_request()` function. This can be used now in all files.

#### **`models.py`**

The models file creates the Event database model which includes the title, description, task_date, completion, priority and username fields (Foreign key).

#### **`tests.py`**

The tests file is for configuring debugging tests.

#### **`urls.py`**

The file contains the url pattern to navigate to the calendar path.

#### **`utils.py`**

This file creates the Calendar object class which writes the methods to configure the calendar days, weeks, months and filters through the database to place the Events in the day cells.

#### **`views.py`**

The views file contains the calendarView which renders all the methods in the `utils.py` file and adds the month name, weekday names, and date numbers. It then returns the completed calendar table.

___

### Planner Module

The planner module is the main app within the project. It contains all the main input forms, save methods and data processing methods needed to perform the main functions in the program.

#### **Static Folder (planner)**

This folder contains the `main.css` file which contains the formatting for the home page, dashboard page, detail page, profile page, login page, and register page.

#### **Template Folder (planner)**

This folder contains the HTML template for the calendar. It containts the `alltasks.html`, `base.html`, `dashboard.html`, `editform.html`, `enter.html`, `footer.html`, `header.html`, `home.html`, `task_detail.html`, `task_form.html` and `topnav.html` files. The alltasks file displays the selected tasks on the dashboard page. The base file inherits its javascript headers and footers from the html files. The dashboard page displays the organized summary of tasks. The editform file displays form to edit tasks. The task detail file displays information on a certain task and the task form file is for the input form. The topnav file displays the navigation bar.

#### **`__init__.py` (planner)**

Empty file which is required within the framework to initialize the planner module.

#### **`admin.py` (planner)**

Admin file registers the Task database model for use.

#### **`apps.py` (planner)**

Apps file initializes the planner module to be able to run the program and reference it from other files

#### **`models.py` (planner)**

The models file creates the Task database model which includes the following fields:

    complete = models.BooleanField(default='False')                                      
    task = models.CharField(max_length=200)                                              
    date_added = models.DateField(default= timezone.now)                                  
    date_added_year = models.CharField(max_length=4,default="0000")                       
    date_added_month = models.CharField(max_length=2, default="00")                       
    date_added_day = models.CharField(max_length=2, default="00")                         
    date_added_week = models.CharField(max_length=2, default="00")                        
    type = models.CharField(max_length=200)                                               
    date = models.DateField(default = datetime.date.today, editable = True, blank = True)  
    desc = models.TextField(max_length=500, default= "enter")                             
    hours_planned = models.IntegerField(default=0)                                        
    hours_worked = models.IntegerField(default=0)                                         
    priority = models.CharField(max_length=32)                                            
    user_written = models.ForeignKey(User, default=1, verbose_name='user', on_delete=models.CASCADE)

#### **`tests.py` (planner)**

The tests file is for configuring debugging tests.

#### **`urls.py` (planner)**

The file contains the url pattern to navigate to the all views within the planner module.

#### **`views.py` (planner)**

The views file contains the views which give context to all the html templates. The methods to save the Event and Task model are also located in there. All the algorithms and database filtering is also located in this folder. Each method redirects to a apecific html file or redirect to the default file which is located in the settings file.

___

### Users Module

The users module contains the user verification system which allows the a user to create an account, login and create a profile. It contains all the login, user and registration form classes as well as the Profile database model.

#### **Template Folder (users)**

This folder contains the HTML template for the calendar. It containts the `login.html`, `loginfirst.html`, `logout.html`, `profile.html`, `register.html`. These files handle the views for the user verification pages.

#### **`__init__.py` (users)**

Empty file which is required within the framework to initialize the users module.

#### **`admin.py` (users)**

Admin file registers the Profile database model for use.

#### **`apps.py` (users)**

Apps file initializes the users module to be able to run the program and reference it from other files.

#### **`models.py` (users)**

The models file creates the Profile model which has two fields: The user and the profile image.

#### **`signals.py` (users)**

The file contains a signal and receiver in order to create a new profile automatically everytime a new user is created.

#### **`tests.py` (users)**

The tests file is for configuring debugging tests.

#### **`views.py` (users)**

The views file contains the views which give context to all the html templates. The methods to save the login, register, user and profile update forms are also located in there. Each method redirects to a apecific html file or redirect to the default file which is located in the settings file.
___

### Settings File

The settings files contains all the imports, middleware initialization, app initialization, external libraries, database configuration and global constant variables which are used throughout the project. It also contain the keys and upload information to upload files to amazon s3 bucket storage since the program is hosted on a web server.
