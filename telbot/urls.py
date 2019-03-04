from django.urls import path
from . import views

urlpatterns=[
	path('',views.get_man,name='index'),
	path('get_man',views.get_man,name='man'),
]
