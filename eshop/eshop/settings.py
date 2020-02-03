"""
Django settings for eshop project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&+_^eprz!soim!-vpmxt5fhv-74h4c3j-_t4h8$knvf5keud(j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'ecommerce.apps.EcommerceConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'carts',
    'orders',
    'user',
    'accounts',
    #'storages',
    #'rest_framework',
    #'files',
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

ROOT_URLCONF = 'eshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'eshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eshop',
        'USER': 'postgres',
        'PASSWORD': 'Lenovok8+',
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PAYMENT_VARIANTS = {
    'razorpay': ('django_payments_razorpay.RazorPayProvider', {
        'public_key': 'rzp_test_9rucf6UibIA2LO',
        'secret_key': 'wGc2DKBbD4eFzIggoA7kXuBI'})}

RAZORPAY_SECRET_KEY = "rzp_test_9rucf6UibIA2LO"


#AWS_ACCESS_KEY_ID='AKIAXYW6QAFX7CKEJGJ3'
#AWS_SECRET_ACCESS_KEY='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'
#AWS_STORAGE_BUCKET_NAME='vishesht'
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL =  None

#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#AWS_S3_OBJECT_PARAMETERS = {
#    'CacheControl': 'max-age=86400',
#}
#AWS_LOCATION = 'static'

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
#]
#STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#######################
AWS_UPLOAD_BUCKET = "cfe-awesome-bucket"

AWS_UPLOAD_USERNAME = "CFE_user_justin"

AWS_UPLOAD_GROUP = "CFE_AwesomeGroup"

AWS_UPLOAD_REGION = 'us-west-2'

AWS_UPLOAD_ACCESS_KEY_ID = "AKIAJQEJZQD6WMEQIK7A"

AWS_UPLOAD_SECRET_KEY = "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"