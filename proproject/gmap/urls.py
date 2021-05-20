from django.urls import path

from .views import index ,ProCreate,listfunc

app_name = 'gmap'
urlpatterns = [
    path('', index, name='index'),
    path('create/',ProCreate.as_view() , name='create'),
    path('list/', listfunc, name='list'),
]





