from django.db import models

# Create your models here.
from django_facebook.models import *
from problems.models import *
class Level(models.Model):
	user_id		=	models.OneToOneField(FacebookCustomUser)
	level_id	=	models.IntegerField()
	profile_id  = 	models.OneToOneField(FacebookProfile)
	
	def __unicode__(self):
		return self.user_id.first_name + "|" + self.level_id

class Help(models.Model):
	help = models.TextField()
class Rules(models.Model):
	rule = models.TextField()
