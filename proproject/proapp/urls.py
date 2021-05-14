from django.contrib import admin
from django.urls import path 
from .views import createfunc

urlpatterns = [
    path('create',createfunc),
    
]