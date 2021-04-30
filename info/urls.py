from django.urls import path
from . import views

urlpatterns= [
	path('', views.home, name= 'info-home'),
    path('covid/', views.covid, name='info-covid'), 
    path('book/', views.book, name='info-book'), 
]