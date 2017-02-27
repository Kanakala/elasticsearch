from django.conf.urls import include, url
from .views import restaurant


urlpatterns = [
	url(r'^code/$', restaurant),
		]