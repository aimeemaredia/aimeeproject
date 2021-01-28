#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    apps.py to configure the user module and user signals 

#imports 
from django.apps import AppConfig

# configure user app
class UsersConfig(AppConfig):
    name = 'users'

    #import signals module for use 
    def ready(self):
        import users.signals
