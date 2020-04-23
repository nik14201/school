from .settings import *


SITE_ID = 4
INSTALLED_APPS += ['rest_framework.authtoken']
AUTH_USER_MODEL = 'parent.Parent'

ACCOUNT_USER_MODEL_USERNAME_FIELD='email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_UNIQUE_EMAIL = True

SITE_NAME = "school"
SITE_DOMAIN = "parent.school.local"
BASE_URL = 'https://parent.school.local'
