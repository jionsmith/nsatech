from django.conf.urls import url
from . import views
from .venu_views import *

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', VenuView.as_view(), name='dashboard.index'),
    url(r'^venu/save/', VenuUpdateView.as_view(), name='venu_save'),
	url(r'^venu/delete/(?P<pk>\d+)/$', VenuDeleteView.as_view(), name='venu_delete'),
]
