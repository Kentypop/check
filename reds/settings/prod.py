import os
from .base import *
#import environ

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'desolate-citadel-45217.herokuapp.com']

LOGGING ={
    'version':1,
    'loggers':{
        'django':{
            'handlers':['file','file2'],
            'level':'DEBUG'
        }
    },
    'handlers':{
        'file':{
            'level':'INFO',
            'class': 'logging.FileHandler',
            'filename':'./logs/debug5.log',
            'formatter':'simpleRe',
        },
        'file2':{
            'level':'DEBUG',
            'class': 'logging.FileHandler',
            'filename':'./logs/debug6.log',
            'formatter':'simpleRe',
        }
    },
    'formatters':{
        'simpleRe': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }

    }
}