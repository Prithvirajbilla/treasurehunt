from django.contrib import admin
from problems.models import *
from django_facebook.models import *
# Register your models here.
from image_cropping import ImageCroppingMixin
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
admin.site.register(Problem,MyModelAdmin)
admin.site.register(FacebookCustomUser)

from login.models import *
admin.site.register(Level)
admin.site.register(Help)
admin.site.register(Rules)