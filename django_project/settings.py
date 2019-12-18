"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json

# load the keys you want to hide from a file (choose whatever file formart you prefer)
with open('path/to/config_file.json') as f:
    config = json.load(f)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY'] # 'qtzcs3y&9*&p2$-6#ytnyq=lu#71x&=j_j5gc@uwj#oooo#syn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.domain_name.suffix', '000.00.000.00']  # enter here as a string the IP-adress or the domain name of your server


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'storages',  # if you use django storages
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

SATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

EMAIL_HOST           = 'smtp.gmail.com'  # use gmail as email host
EMAIL_PORT           = 587
EMAIL_HOST_USER      = config.get('EMAIL_USER') 
EMAIL_HOST_PASSWORD  = config.get('EMAIL_PASSWORD')
EMAIL_USE_TLS        = True
DEFAULT_FROM_EMAIL   = EMAIL_HOST_USER
EMAIL_FROM           = EMAIL_HOST_USER
EMAIL_SUBJECT_PREFIX = '[Project] '
EMAIL_BACKEND        = 'django.core.mail.backends.smtp.EmailBackend'

# ADMINS and MANAGERS, set as many as you like
ADMINS = [('Website Admin', 'website.admin@example.com')]
MANAGERS = ADMINS + [('Website Manager', 'website.manager@example.com')]


""" if you work with a Amazon Web Services S3 bucket
get the secret keys from the environment variables
AWS_ACCES_KEY_ID = os.envirion.get('AWS_ACCES_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.envirion.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.envirion.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False  # prevent the bucket from overwriting e.g. files loaded up which have the same name
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
"""