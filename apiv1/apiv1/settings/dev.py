#* 开发阶段的配置文件

import os,datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j20u!+%+1v5rzq#k%4=1gb!y05*lyct242hf!yht&o09u^+4-z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    # 'course.apps.CourseConfig',
    'utils.apps.UtilsConfig',


    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
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
]

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
        'NAME': 'pcw',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':  '127.0.0.1',
        'PORT': 3306,
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
AUTH_USER_MODEL = "users.AdminUser"



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
              'rest_framework.authentication.TokenAuthentication',       # 首先进行token认证
              'rest_framework.authentication.SessionAuthentication',     # 
              'rest_framework.authentication.BasicAuthentication',       
          ),
        }

# 配置redis数据库
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        "OPTIONS": {
        },
    },
    "session": {  # 存储 session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
        },
    },
    "verify_code": {  # 存储 验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
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
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
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





