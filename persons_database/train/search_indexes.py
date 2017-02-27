from django.utils import timezone
from haystack import indexes
from .models import Restaurant
from datetime import datetime

class RestaurantIndex(indexes.SearchIndex, indexes.Indexable):

	text = indexes.CharField(document=True, use_template=True)
	code = indexes.CharField(model_attr='code')
	
	def get_model(self):
		return Restaurant
		
	def no_query_found(self):
		return self.searchqueryset.exclude(code='code 998')

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.all()
		