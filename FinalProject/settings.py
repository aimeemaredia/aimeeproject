#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    settings.py file for all application settings such as app registration, middleware, database connections
#    debugging variables and setting storage variables  

#imports 
import os
from pathlib import Path
import django_heroku


# define base subdirectory 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#the allowed hosts are the heroku web server and my localhost server 
ALLOWED_HOSTS = ['aimeeplannerproject.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'cal.apps.CalConfig',          # cal module
    'jquery',                      # jquery app
    'users.apps.UsersConfig',      # users module
    'planner.apps.PlannerConfig',  # planner module
    'crispy_forms',                # crispy form rendering 
    #default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

# middleware registration 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'cal.middleware.RequestMiddleware',                        #my custom middleware file 
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

# root url path 
ROOT_URLCONF = 'FinalProject.urls'

# local template configuration 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'FinalProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# local template configuration 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'final_data',
        'USER': 'root',
        'PASSWORD': 'Snowell374!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }    
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


#define media root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#define media url 
MEDIA_URL = '/media/'
#define bootstrap for crispy template 
CRISPY_TEMPLATE_PACK = 'bootstrap4'
#change the default storage 
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#default redirect page 
LOGIN_REDIRECT_URL = 'planner-home'
#default login url 
LOGIN_URL = '/'
#access key environment variable for amazon s3 data storage 
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#secret access key environment variable for amazon s3 data storage 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#amazon s3 bucket name 
AWS_STORAGE_BUCKET_NAME = 'compsci-planner-project'
#amazon s3 region 
AWS_S3_REGION_NAME = 'us-east-2' 
#set rewrite to false (same name)
AWS_S3_FILE_OVERWRITE = False
#set default acl to none
AWS_DEFAULT_ACL = None
#set aws custom domain
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#set aws object parameters 
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
#set aws location 
AWS_LOCATION = 'static'
#define static url
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}/'
#define static storage
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


#set the heroku setting as the local settings 
django_heroku.settings(locals())