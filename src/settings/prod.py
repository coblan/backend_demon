from .base import *
import pymysql

pymysql.install_as_MySQLdb()


DATABASES = {
     'default': {
        'NAME': 'backend_demo',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'zhou',
        'PASSWORD': 'zhou570508',
        'HOST': '172.18.215.159', 
        'PORT': '3306', 
        'OPTIONS': {'charset':'utf8mb4'},

      },
} 

ALLOWED_HOSTS=['*']

SELF_DOMAIN='http://demo.softjing.com'

INSPECT_DICT_STATIC = 'D:\work\part3\backend_demon\src\index.py'