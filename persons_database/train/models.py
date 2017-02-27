from django.db import models

class Restaurant(models.Model):
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name
		
	def __str__(self):
		return self.name