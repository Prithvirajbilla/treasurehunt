import os
import sys      
sys.path.append('/var/www/treasurehunt/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'treasurehunt.settings-production'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

