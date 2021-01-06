"""
Django settings for maskes project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import django_heroku
import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'build')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'THIS-IS-A-DUMMY-KEY'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'users.apps.UsersConfig',
    'requests.apps.RequestsConfig',
    'offers.apps.OffersConfig',
    'events.apps.EventsConfig',
    'funds.apps.FundsConfig',
    'connect.apps.ConnectConfig',
    'templated_mail',
    'ckeditor',   
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maskes.middleware.AdminTimezoneMiddleware',
]

ROOT_URLCONF = 'maskes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
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

WSGI_APPLICATION = 'maskes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maskes',
        'USER': 'maskes',
        'PASSWORD': 'maskes',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# If True, the whitelist will not be used and all origins will be accepted. Defaults to False.
CORS_ORIGIN_ALLOW_ALL = True

# Assigns read+write to user, and read only to group
FILE_UPLOAD_PERMISSIONS = 0o640

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 21
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

DOMAIN = 'localhost:3000'
SITE_NAME = 'skcema'

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset-confirm/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_URL': 'email-reset-confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_RETYPE': True,
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
    },
    'HIDE_USERS': True,
}

#Email will be setup in local_setting.py using environment variables
#SECURITY WARNING: don't put your email info here
#django dummy email backend will not send any email
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


AUTH_USER_MODEL = 'users.UserAccount'

JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'SKCEMA Admin Portal',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'SKCEMA Admin',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # 'site_logo': 'polls/img/logo.png',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to Mutual Aid South King County & East Side Portal',

    # Copyright on the footer
    'copyright': 'SKCEMA',

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'users.UserAccount',

    # 'hide_apps': ['authtoken','token_blacklist'],

    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},

        # external url that opens in a new window (Permissions can be added)
        {'name': 'Site', 'url': 'https://skcema.org/', 'new_window': True},

        # model admin to link to (Permissions checked against model)
        {'model': 'users.UserAccount'},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'requests'},
    ],

    'usermenu_links': [
        {'name': 'Profile', 'url': 'http://localhost:3000/profile/me/', 'new_window': True},
    ],

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': ['token_blacklist', 'authtoken',],

    'show_sidebar': True,

    'order_with_respect_to': ['requests', 'funds', 'users', 'connect'],

    # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    'icons': {
        'users': 'fas fa-users-cog',
        'users.UserAccount': 'fas fa-user',
        'users.UserAddress': 'fas fa-map-marked',
        'users.UserProfile': 'fas fa-address-card',
        'auth.Group': 'fas fa-users',
        'requests.Request': 'fas fa-mail-bulk',
        'requests.Volunteer': 'fas fa-project-diagram',
        'funds.Reimbursement': 'fas fa-comment-dollar',
        'funds.Donation': 'fas fa-dollar-sign',
        'connect.Comment': 'fas fa-comments',
        'connect.Reply': 'fas fa-reply',
    },

    # Field name on user model that contains avatar image
    'user_avatar': 'users.UserProfile.image',

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-lightblue",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full'
    },
}

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"


# Activate Django-Heroku.
django_heroku.settings(locals())

try:
  from .local_settings import *
except ImportError:
  pass
