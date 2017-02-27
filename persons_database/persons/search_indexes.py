from haystack import indexes

from .models import Restaurant


class RestaurantIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	restaurant = indexes.CharField(model_attr='restaurant')
	code = indexes.CharField(model_attr='code')

	def get_model(self):
		return Restaurant
