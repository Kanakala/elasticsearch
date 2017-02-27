from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from persons.views import CustomSearchView
from haystack.query import SearchQuerySet
from haystack.forms import ModelSearchForm, SearchForm
from haystack.views import SearchView
from django.conf.urls import *
import json
from urllib.request import urlopen


sqs = SearchQuerySet().all()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^search/', CustomSearchView, name='haystack_search'),
    
]

