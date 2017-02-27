from django import forms
from haystack.forms import SearchForm

class CustomSearchForm(SearchForm):

	search_string = forms.CharField()
	def search(self):
		object_list = super(CustomSearchForm, self).search()
		if not self.is_valid():
			return self.no_query_found()

		if self.cleaned_data['search_string']:
			object_list = object_list.filter(code=self.cleaned_data['search_string'])
			
		return object_list