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

### NPC Class

Class `NPC` inherits from class `BaseCharacter` and also stores the enemy damage number for the enemy. It is stored in the `attackDamage` variable. The method attack is used to attack player characters and reduce their health. The `printLife` method is used to print the updated life of any character.

___

### PC Class

Class `PC` initiates the `BaseCharacter` class and the `Weapon` class to create a player. Instances of this class are the player and a weapon is associated with each one.

___

### Enemy Class

Class `Enemy` initiates the `BaseCharacter` class and instances of this class are NPC.

___

### Friend Class

Class `Friend` initiates the `BaseCharacter` class and instances of this class are NPC.
