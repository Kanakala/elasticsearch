from django.contrib import admin
from django.db import models
from .models import Restaurant

class RestaurantModelAdmin(admin.ModelAdmin):
    
    class Meta:
            model = Restaurant

admin.site.register( Restaurant, RestaurantModelAdmin)