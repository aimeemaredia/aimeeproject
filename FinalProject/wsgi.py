#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    wsgi.py file settings 

"""
WSGI config for FinalProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')
#os.environ["DJANGO_SETTINGS_MODULE"] = "FinalProject.settings"


application = get_wsgi_application()
