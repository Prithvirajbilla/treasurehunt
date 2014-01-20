from django.db import models

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', filename])
from image_cropping import ImageRatioField

class Problem(models.Model):
	title 		=	models.CharField(max_length=255,null=True,blank=True)
	question	=	models.CharField(max_length=1000,null=True,blank=True)
	answer		= 	models.CharField(max_length=30)
	picture		= 	models.ImageField(upload_to=content_file_name,null=True,blank=True)
	hints		= 	models.TextField(null=True,blank=True)
	clues		= 	models.TextField(null=True,blank=True)
	map_data	= 	models.TextField(null=True,blank=True)
	type_data 	= 	models.BooleanField(default=True)
	form_data   = 	models.TextField()
	other_data  =   models.TextField()
	cropping = ImageRatioField('picture', '640x480',size_warning=True)

	def __unicode__(self):
		return self.title +' | '+self.answer
