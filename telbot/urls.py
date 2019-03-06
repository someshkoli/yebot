from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns=[
#	url('',views.get_man,name='index'),
	url(r'\w*',views.index,name='index'),
#	url('up',views.up,name='up'),
]
