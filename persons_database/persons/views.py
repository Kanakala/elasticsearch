from haystack.forms import SearchForm, ModelSearchForm
from .forms import CustomSearchForm
from haystack.query import SQ, SearchQuerySet
from haystack.views import SearchView, basic_search, search_view_factory
import json
from urllib.request import urlopen
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext

# class CustomSerchView(SearchView):

	# template_name = 'templates/search/search.html'
    # queryset = SearchQuerySet().all()
    # form_class = SearchForm
	
	# def form_valid(self, form):
		# a = self.request.POST['train'])
		# return super(CustomSearchView, self).form_valid(form)
		
	# def get_queryset(self):
        # queryset = super(CustomSearchView, self).get_queryset()
        #further filter queryset based on some set of criteria
        # return queryset.filter(pub_date__gte=date(2015, 1, 1))
		
		
		
def CustomSearchView(request):
	#form = CustomSearchForm(request.GET)
	#search_string = request.GET.get('q', '')
	#response = urlopen("http://api.railwayapi.com/route/train/search_string/apikey/3dacdecg/").read().decode('utf8')
	#obj = json.loads(response)
	#x = obj['route']
	#b = [a['code'] for a in x]
	object_list = SearchQuerySet().all()
	
	view = search_view_factory(
        view_class=SearchView,
        template='search/search.html',
        searchqueryset=object_list,
        form_class=SearchForm
        )
	
	# context= {
		# 'object_list': object_list,
		# 'form':form,
		# }
	return view(request)