from django.contrib import admin
from django.urls import path 
from .views import listfunc


urlpatterns = [
    path('list/',listfunc,name='list')
    
]