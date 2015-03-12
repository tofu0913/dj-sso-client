"""
Django settings for ssoclient project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'er&14^+l(t-czhaebnta-&!9bt(x%@$9zozoq!ui4!)w0#9=c3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djssoclient',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ssoclient.urls'

WSGI_APPLICATION = 'ssoclient.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )


# ssoclient application settings
SSO_USER_STORAGE = "djssoclient.userstorage.SSOUserCacheStorage"
# SSO_SETTING_CACHE = "default"  # default

SSO_API_AUTH_SETTING = {
    "apikey": "f4a05287",
    "seckey": "6a4eeaea54d54f51af703e79c6096d51",
    "url": "https://dj-sso-sample.herokuapp.com",
}
SSO_REMOTE_URL_PREFIX = "/sso/"

AUTHENTICATION_BACKENDS = ("djssoclient.authbackend.SSOAuthBackend",)
AUTH_USER_MODEL = "djssoclient.SSOUser"

LOGIN_REDIRECT_URL = "/"