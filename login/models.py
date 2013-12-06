from django.db import models

# Create your models here.
from django_facebook.models import *
from problems.models import *

class Level(models.Model):
	user_id		=	models.ForeignKey(FacebookCustomUser)
	level_id	=	models.IntegerField()
