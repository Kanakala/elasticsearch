from django.db import models



class Restaurant(models.Model):
	restaurant = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	
	def __str__(self):
		return self.restaurant
