from django.db import models

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class Problem(models.Model):
	title 		=	models.CharField(max_length=15,null=True,blank=True)
	question	=	models.CharField(max_length=1000,null=True,blank=True)
	answer		= 	models.CharField(max_length=30)
	picture		= 	models.ImageField(upload_to=content_file_name,null=True,blank=True)
	hints		= 	models.TextField(null=True,blank=True)
	clues		= 	models.TextField(null=True,blank=True)

