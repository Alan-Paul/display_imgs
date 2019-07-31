"""
Django settings for main_settings project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i(ulp4so+6lc^67lwsxkxx#j4hor))vegw(fqq-9o%odtkti#a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']#跨ip访问

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'display_img',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS')
CORS_ALLOW_HEADERS = ('x-requested-with', 'content-type', 'accept', 'origin', 'authorization', 'x-csrftoken')

ROOT_URLCONF = 'main_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]
WSGI_APPLICATION = 'main_settings.wsgi.application'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static');
STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("img", os.path.join(STATIC_ROOT,'img')),
    ("font", os.path.join(STATIC_ROOT,'font')),
)
IMG_ROOT = "/ssd2/lin/lsc/dataset_reid/market/bounding_box_train/"
IMG_LIST = "/home/ltb/myshare/tornado_visualizer/img_path_list/train.txt"
IMG_PER_PAGE = 20
