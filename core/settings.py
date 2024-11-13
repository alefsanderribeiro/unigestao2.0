from dotenv import load_dotenv
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%)eo!m%!t7r=x5uo$i52^au_$e-r7d-7%1wk9&y+5#*y+=&swb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # App de Interface
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'employees',
    'geography',
    'cbos',
    'bond',
    'configurations',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'base_templates'
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DOCKER_MODE = False  # Altere para False para usar SQLite

if DOCKER_MODE:
    load_dotenv()
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = ['static',]
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, './media')
MEDIA_URL = '/media/'


THOUSAND_SEPARATOR = '.',
USE_THOUSAND_SEPARATOR = True


JAZZMIN_SETTINGS = {
    # título da janela (Será o valor padrão de current_admin_site.site_title se ausente ou None)
    'site_title': 'SGP',

    # Título na tela de login (máximo de 19 caracteres) (padrão é current_admin_site.site_header se ausente ou None)
    'site_header': 'Uni Gestão',

    # Título na marca (máximo de 19 caracteres) (padrão é current_admin_site.site_header se ausente ou None)
    'site_brand': 'Uni Gestão (SGP)',

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',

        # App Employees
        'employees.Employee': 'fa-solid fa-address-book',


        # App Geography
        'geography.City': 'fa-solid fa-city',
        'geography.State': 'fa-solid fa-compass',
        'geography.Country': 'fa-solid fa-earth-americas',

        # App 'configurations' (exemplo para os modelos que você deseja agrupar)
        'configurations.AdmissionType': 'fa-solid fa-cogs',  # Adiciona um ícone ao modelo
        'configurations.HarmfulExposure': 'fa-solid fa-biohazard',  # Exemplo de ícone
        'configurations.PaymentType': 'fa-solid fa-credit-card',  # Ícone para Tipo de Pagamento
        'configurations.Bank': 'fa-solid fa-university',  # Ícone para Banco
        'configurations.AccountType': 'fa-solid fa-wallet',  # Ícone para Tipo de Conta
        'configurations.PixType': 'fa-solid fa-qrcode',  # Ícone para Tipo de Pix
        'configurations.MaritalStatus': 'fa-solid fa-hand-holding-heart',
        'configurations.Deficiency': 'fa-solid fa-wheelchair',
        'configurations.DegreeInstruction': 'fa-solid fa-file-contract',
        'configurations.Nationality': 'fa-solid fa-earth-americas',
        'configurations.Race': 'fa-solid fa-hands-holding-circle',
    },

    # Texto de boas-vindas na tela de login
    'welcome_sign': 'Bem-vindo(a) ao Uni Gestão (SGP)',

    # Copyright no rodapé
    'copyright': 'Coding Solutions LTDA',

    # Lista de administradores de modelos a serem pesquisados na barra de pesquisa, barra de pesquisa será omitida se excluída
    'search_model': ['employees.Funcionario',],

    # Se deve mostrar o personalizador de UI na barra lateral
    # 'show_ui_builder': True,

    # Ordenação de modelos
    'order_with_respect_to': [
        'auth',  # Coloca o app 'auth' no topo
        'employees',  # Coloca o app 'employees' após 'auth'
        'bond',
        'configurations',
        'configurations.bank',  # Dentro do app 'configurations', ordena os modelos
        'configurations.accounttype',  # Dentro do app 'configurations', ordena os modelos
        'configurations.paymenttype',  # Dentro do app 'configurations', ordena os modelos
        'configurations.pixtype',  # Dentro do app 'configurations', ordena os modelos
    ],

    # apps não listados
    # "hide_apps": ['geography',],

    # models não listados
    "hide_models": ['bond.AdmissionInfo'],

    "custom_links": {
        "bond": [{
            # Qualquer nome que você preferir
            "name": "Gerenciar Vinculo",

            # nome da URL, ex: `admin:index`, URLs relativas, ex: `/admin/index` ou URLs absolutas, ex: `https://domain.com/admin/index`
            "url": "admin:bond_admissioninfo_changelist",

            # qualquer ícone do Font Awesome, veja a lista aqui https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2 (opcional)
            "icon": "fas fa-briefcase",

            # uma lista de permissões que o usuário deve ter para ver este link (opcional)
            # "permissions": ["bond.view_admissioninfo"]     
        }]
    },

}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}
