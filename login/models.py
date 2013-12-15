from django.db import models

# Create your models here.
from django_facebook.models import *
from problems.models import *
class Level(models.Model):
	user_id		=	models.OneToOneField(FacebookCustomUser)
	level_id	=	models.IntegerField()
	profile_id  = 	models.OneToOneField(FacebookProfile)

class Help(models.Model):
	help = models.TextField()
class Rules(models.Model):
	rule = models.TextField()
