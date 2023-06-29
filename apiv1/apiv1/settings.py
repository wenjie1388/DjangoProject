#* 开发阶段的配置文件

import os,datetime
from apiv1.dev import *
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j20u!+%+1v5rzq#k%4=1gb!y05*lyct242hf!yht&o09u^+4-z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG__
ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'article.apps.ArticleConfig',
    # 'course.apps.CourseConfig',
    'utils.apps.UtilsConfig',
    'auths.apps.AuthsConfig',

    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
]
# from django.middleware.security import SecurityMiddleware
MIDDLEWARE = [
    # 跨域中间件 
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
from django.contrib.sessions.middleware import SessionMiddleware
ROOT_URLCONF = 'apiv1.urls'

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

WSGI_APPLICATION = 'apiv1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQLNAME,
        'USER':MYSQLUSER,
        'PASSWORD':MYSQLPASSWORD,
        'HOST':  MYSQLHOST,
        'PORT': MYSQLPORT,
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####################### 用于验证的模型
AUTH_USER_MODEL = "users.Admin"



# *===============================================* #
# ******************** 跨域配置 ******************** #
# *===============================================* #

CORS_ALLOW_CREDENTIALS = True # 允许携带cookies
CORS_ORIGIN_ALLOW_ALL = True

# 跨域白名单
# CORS_ORIGIN_WHITELIST = [
#     '127.0.0.1:5173',
#     '127.0.0.1:8000',
# ]



CORS_ORIGIN_WHITELIST = ()
# 对应的发送的请求的跨域
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)


# *================================================ #
# *************** REST_FRAMEWORK配置 *************** #
# *================================================ #
REST_FRAMEWORK = {
          'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
              # 'rest_framework.authentication.TokenAuthentication',       # 首先进行token认证
              # 'rest_framework.authentication.SessionAuthentication',     # 
              # 'rest_framework.authentication.BasicAuthentication',       
          ),
          'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
          'PAGE_SIZE': 10
        }
from rest_framework.authentication import SessionAuthentication
# 配置redis数据库
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS1_LOCATION,
        "OPTIONS": {
        },
    },
    "session": {  # 存储 session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS2_LOCATION,
        "OPTIONS": {
        },
    },
    "verify_code": {  # 存储 验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS3_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "CONNECTION_POOL_KWARGS": {"max_connections": 100}, # 最大的连接池数量，django-redis 使用 redis.py 的连接池，默认不关闭连接，尽可能重用连接 
        },
    },
    "token": {  # 存储 验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS3_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
    "staks": {  # 存储 验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS10_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "CONNECTION_POOL_KWARGS": {"max_connections": 100}, # 最大的连接池数量，django-redis 使用 redis.py 的连接池，默认不关闭连接，尽可能重用连接 
        },
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# 文件和图片上传配置
MEDIA_ROOT = os.path.join(BASE_DIR, '../upload')
MEDIA_URL = '/media/'


# *===============================================* #
# ******************** DRF 配置 ******************** #
# *===============================================* #
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        "rest_framework.authentication.BasicAuthentication",
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}


JWT_AUTH = {
    # token有效期为24小时
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from django.utils.translation 



# =============================================== #
# **************** 发送邮箱 配置 ***************** #
# =============================================== #
EMAIL_BACKEND = EMAIL_BACKEND1
EMAIL_HOST = EMAIL_HOST1
EMAIL_PORT = EMAIL_PORT1  
EMAIL_HOST_USER = EMAIL_HOST_USER1
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD1  
EMAIL_USE_TLS = EMAIL_USE_TLS1  
EMAIL_FROM = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER




# =============================================== #
# **************** 日志 配置 ***************** #
# =============================================== #

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     },
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    'handlers': {
        'console': {
            'level': 'INFO',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            # 'filters': ['special']
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'level': 'DEBUG',
            # 'class': 'logging.FileHandler',
            'class': "logging.FileHandler",
            'filename':'log/log.txt',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            # 'handlers': ['mail_admins'],
            'handlers': ['file',],
            # 'level': 'ERROR',
            'level': 'DEBUG',
            # * propagate 是指
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            # 'filters': ['special']
        }
    }
}





