from django.shortcuts import render_to_response

from .forms import RestaurantSearchForm
from haystack.query import SearchQuerySet


def restaurant(request):
	form = RestaurantSearchForm(request.GET)
	search_string = request.GET.get('search_string', '')
	restaurants = []

	sqs = SearchQuerySet().filter(search_tags=search_string)

	restaurants = [a.object for a in sqs[0:10]]

    #restaurants = form.search()
	return render_to_response('search/codes.html', {'restaurants': restaurants})