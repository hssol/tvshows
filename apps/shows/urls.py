from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shows),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new),
    url(r'^add_show$', views.add_show),
    url(r'^shows/(?P<id>\d+)$', views.display_show),
    url(r'^shows/(?P<id>\d+)/edit$', views.edits),
    url(r'^delete_show/(?P<id>\d+)$', views.delete_show),
    url(r'^edit_show/(?P<id>\d+)$', views.edit_show)
]