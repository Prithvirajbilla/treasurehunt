from django.contrib import admin
from problems.models import *
from django_facebook.models import *
# Register your models here.
admin.site.register(Problem)
admin.site.register(FacebookCustomUser)

from login.models import *
admin.site.register(Level)
admin.site.register(Help)
admin.site.register(Rules)