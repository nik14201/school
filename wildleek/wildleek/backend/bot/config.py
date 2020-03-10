import sys, os
sys.path.insert(0, './../django/www/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'etc.settings'
import django; django.setup()

TOKEN = '***************************'
