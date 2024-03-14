from pathlib import Path
from decouple import config, Csv
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

DJANGO_APPS = [
    'accounts',
    'core',
    'stores',
    'products',
    'orders',
    'reviews',
    'notifications',
    'loyalty'
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'corsheaders',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + THIRD_PARTY_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CardapioRapido_project.urls'

CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'CardapioRapido_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]
""" {
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
    }, """


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}


""" 
DEFAULT_RENDERER_CLASSES: Define os renderizadores padrão para a API. 
Neste exemplo, estamos usando JSONRenderer para renderizar dados em
JSON e BrowsableAPIRenderer para fornecer uma interface de API navegável.
DEFAULT_PARSER_CLASSES: Define os analisadores padrão para a API. 
Estamos usando JSONParser para analisar dados JSON, FormParser 
para analisar dados de formulários e MultiPartParser para 
analisar dados de upload de arquivos.
DEFAULT_AUTHENTICATION_CLASSES: Define as classes de autenticação 
padrão para a API. Neste exemplo, estamos usando 
SessionAuthentication para autenticação baseada em sessão e 
BasicAuthentication para autenticação básica.
DEFAULT_PERMISSION_CLASSES: Define as classes de permissão padrão para a API. 
Neste exemplo, estamos exigindo que o usuário 
esteja autenticado para acessar a API.
DEFAULT_PAGINATION_CLASS: Define a classe de paginação padrão. 
Neste exemplo, estamos usando PageNumberPagination para paginar os resultados.
PAGE_SIZE: Define o tamanho padrão da página para a paginação.
DEFAULT_FILTER_BACKENDS: Define os filtros padrão para a API. 
Neste exemplo, estamos usando DjangoFilterBackend para 
filtrar por campos do modelo, SearchFilter para pesquisar por 
campos de texto e OrderingFilter para ordenar os resultados.
"""


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'accounts.User'

""" AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 'accounts.backends.EmailBackend'
] """


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
