from django.urls import path

from .views import index ,ProCreate,listfunc,pin,detailfunc,signupfunc,loginfunc,logoutfunc,ProDelete,ProUpdate

app_name = 'gmap'
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupfunc ,name='signup'),
    path('login/', loginfunc ,name='login'),
    path('logout/',logoutfunc, name='logout'),
    path('create/',ProCreate.as_view() , name='create'),
    path('list/', listfunc, name='list'),
    path('pin/',pin, name='pin'),
    path('detail/<int:pk>', detailfunc ,name='detail'),
    path('delete/<int:pk>',ProDelete.as_view(),name='delete'),
    path('update/<int:pk>',ProUpdate.as_view(),name='update')

]





