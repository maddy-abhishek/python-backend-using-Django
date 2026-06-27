"""
Advanced Authentication Settings for Django Tweet App
Extends base settings.py with OAuth2, JWT, and Email Verification
"""

from pathlib import Path
import os
from datetime import timedelta

# ============================================
# OAUTH2 & SOCIAL AUTHENTICATION (Google Login)
# ============================================

OAUTH_PROVIDERS = {
    'google': {
        'KEY': os.environ.get('GOOGLE_OAUTH_KEY', 'YOUR_GOOGLE_OAUTH_KEY'),
        'SECRET': os.environ.get('GOOGLE_OAUTH_SECRET', 'YOUR_GOOGLE_OAUTH_SECRET'),
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Add to INSTALLED_APPS:
SOCIAL_AUTH_APPS = [
    'social_django',
]

# Authentication backends for OAuth2
AUTHENTICATION_BACKENDS = (
    # Django default
    'django.contrib.auth.backends.ModelBackend',
    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',
)

# Social Auth URLs
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/tweet/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/tweet/'

# ============================================
# JWT AUTHENTICATION
# ============================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.environ.get('JWT_SECRET_KEY', 'your-secret-key'),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# ============================================
# EMAIL VERIFICATION & CELERY
# ============================================

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your-email@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your-app-password')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@tweetapp.com')

# Email Verification Token Expiry (in seconds)
EMAIL_VERIFICATION_EXPIRY = 24 * 60 * 60  # 24 hours

# Celery Configuration
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# ============================================
# ADDITIONAL SECURITY SETTINGS
# ============================================

# CORS for API requests
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    os.environ.get('FRONTEND_URL', 'http://localhost:3000'),
]

# Secure Cookies (enable in production)
if not os.environ.get('DEBUG', False):
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_HTTPONLY = True
