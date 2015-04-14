#!/usr/bin/python
#encoding=utf-8

"""
Django settings for sellfruit_wecharweb_python project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e!44an2zbfu-$w+y54s@f=5&d^$1@6k0@%-@56f4lo=29fv+)q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = '*'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
     'django.contrib.staticfiles',
     'sellfruit',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'sellfruit_wecharweb_python.urls'

WSGI_APPLICATION = 'sellfruit_wecharweb_python.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fruit',
        'USER':'root',
        'PASSWORD': 'crz332066279',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static')

STATIC_URL = '/static/'


#加载模板
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),

    #('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
)

# STATICFILES_DIRS = (
#     os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
# )
#
# #加入：
# HERE = os.path.dirname(os.path.dirname(__file__))
# #修改：
# MEDIA_ROOT = os.path.join( HERE ,'media').replace('\\','/')
# MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(HERE,'static').replace('\\','/')
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#    os.path.join(HERE,'sellfruit/templates/static/').replace('\\','/'),
# )
# #推荐的做法是将静态文件保存在app下的static目录中。