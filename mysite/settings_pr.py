import os
gettext = lambda s: s

def load(file):
    with open('/etc/cosmosapp/' + file + '.txt') as f:
        return f.read().strip()

DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = load('secret_key')

TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder', 'src', 'height', 'width')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '95.85.38.240', 'cosmostue.nl']

# Application definition
ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.security.SecurityMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.utils.translation',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'djangocms_snippet',
    'mysite',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_googlemap',
    'djangocms_video',
)

FB_PAGE_ID = '1412994915461745'

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'redirect_on_fallback': True,
            'hide_untranslated': False,
            'public': True,
            'code': 'en',
            'name': gettext('en'),
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('registration/login.html', 'Login Page'),
    ('profile.html', 'Profile Page'),
    ('registration/join.html', 'Join Page')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    # Connection to the sqlite db
    # 'default': {
    #     'CONN_MAX_AGE': 0,
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'HOST': 'localhost',
    #     'NAME': 'project.db',
    #     'PASSWORD': '',
    #     'PORT': '',
    #     'USER': ''
    # },

    # Connection to the remote mysql database
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': load('db_name'),
        'USER': load('db_user'),
        'PASSWORD': load('db_password'),
        'HOST': load('db_host'),   # Or an IP Address that your DB is hosted on
        'PORT': load('db_port'),
    }
}

MIGRATION_MODULES = {

}
LOGIN_URL ='/login/'
LOGIN_REDIRECT_URL = '/login/'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'nielsdejong.nl'

# Port for sending e-mail.
EMAIL_PORT = 587

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'cosmos@3ms.nl'
EMAIL_HOST_PASSWORD = 'antsinmyeyes'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'cosmos@3ms.nl'


# Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
#SESSION_COOKIE_SECURE = True

# Using an HttpOnly CSRF cookie makes it more difficult for cross-site scripting attacks to steal the CSRF token.
CSRF_COOKIE_HTTPONLY = True

# Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
#CSRF_COOKIE_SECURE = True

# The default is 'SAMEORIGIN', but unless there is a good reason for your site to serve
# other parts of itself in a frame, you should change it to 'DENY'.
#X_FRAME_OPTIONS = 'DENY'

# If False, your pages will not be served with an 'x-content-type-options: nosniff' header. You should consider enabling
# this header to prevent the browser from identifying content types incorrectly.
SECURE_CONTENT_TYPE_NOSNIFF = True

# If false, your pages will not be served with an 'x-xss-protection: 1; mode=block' header. You should consider enabling
#  this header to activate the browser's XSS filtering and help prevent XSS attacks.
SECURE_BROWSER_XSS_FILTER = True

