from pathlib import Path
import os

# ── Carga del .env ANTES de cualquier otra cosa ────────────────────────────
_BASE = Path(__file__).resolve().parent.parent
_ENV  = _BASE / '.env'

if _ENV.exists():
    for _enc in ('utf-8-sig', 'utf-8', 'latin-1', 'cp1252'):
        try:
            with open(_ENV, encoding=_enc) as _f:
                for _line in _f:
                    _line = _line.strip()
                    if not _line or _line.startswith('#') or '=' not in _line:
                        continue
                    _key, _, _val = _line.partition('=')
                    os.environ.setdefault(_key.strip(), _val.strip())
            break
        except (UnicodeDecodeError, Exception):
            continue

BASE_DIR = _BASE

# ── Seguridad ──────────────────────────────────────────────────────────────
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me')
DEBUG      = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ── Apps ───────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portafolio',
    'contacto',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'impactoweb.urls'

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

WSGI_APPLICATION = 'impactoweb.wsgi.application'

# ── Base de datos PostgreSQL ───────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     os.environ.get('DB_NAME',     'impactoweb_db'),
        'USER':     os.environ.get('DB_USER',     'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST':     os.environ.get('DB_HOST',     'localhost'),
        'PORT':     os.environ.get('DB_PORT',     '5432'),
        'CONN_MAX_AGE': 60,
    }
}

# ── Validación de contraseñas ──────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internacionalización ───────────────────────────────────────────────────
LANGUAGE_CODE = 'es-ec'
TIME_ZONE     = 'America/Guayaquil'
USE_I18N = True
USE_TZ   = True

# ── Archivos estáticos y media ─────────────────────────────────────────────
STATIC_URL  = '/static/'
_static_dir = BASE_DIR / 'static'
STATICFILES_DIRS = [_static_dir] if _static_dir.exists() else []
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Email ──────────────────────────────────────────────────────────────────
EMAIL_BACKEND = (
    'django.core.mail.backends.smtp.EmailBackend'
    if not DEBUG
    else 'django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST          = os.environ.get('EMAIL_HOST',     'smtp.gmail.com')
EMAIL_PORT          = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER',     '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL  = os.environ.get('DEFAULT_FROM_EMAIL',  'ImpactoWeb <hola@impactoweb.agency>')
CONTACT_EMAIL       = os.environ.get('CONTACT_EMAIL',       'hola@impactoweb.agency')

# ── Sesiones ───────────────────────────────────────────────────────────────
SESSION_COOKIE_AGE            = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ── Límite de subida de archivos ───────────────────────────────────────────
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

# ── Seguridad extra en producción (DEBUG=False) ────────────────────────────
if not DEBUG:
    SECURE_SSL_REDIRECT              = True
    SECURE_PROXY_SSL_HEADER          = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS              = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS   = True
    SECURE_HSTS_PRELOAD              = True
    SESSION_COOKIE_SECURE            = True
    CSRF_COOKIE_SECURE               = True
    SESSION_COOKIE_HTTPONLY          = True
    CSRF_COOKIE_HTTPONLY             = True
    SECURE_BROWSER_XSS_FILTER        = True
    SECURE_CONTENT_TYPE_NOSNIFF      = True
    X_FRAME_OPTIONS                  = 'DENY'
    SECURE_REFERRER_POLICY           = 'strict-origin-when-cross-origin'
