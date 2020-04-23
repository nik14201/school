from .settings import *

SITE_ID = 3
INSTALLED_APPS += ['rest_framework.authtoken']
AUTH_USER_MODEL = 'student.Student'

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_UNIQUE_EMAIL = True

SITE_NAME = "school"
SITE_DOMAIN = "student.school.local"
BASE_URL = 'https://student.school.local'