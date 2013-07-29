from django.conf.urls.defaults import *





urlpatterns = patterns('webapp2.views',url(r'^search_form/$','search_form'),url(r'^search/$', 'search'),)
