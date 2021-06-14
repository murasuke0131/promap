from .models import Customer
from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView,DeleteView,UpdateView
from .models import Customer
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login ,logout


def signupfunc(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('gmap:list')
        except IntegrityError:
            return render(request, 'gmap/signup.html', {'error': 'そのユーザーはすでに登録されています。'})
    return render(request, 'gmap/signup.html', {})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gmap:list')   
        else:
            return render(request,'gmap/login.html',{})
    return render(request,'gmap/login.html',{})
    

def logoutfunc(request):
    logout(request)    
    return redirect('gmap:login')

class ProDelete(DeleteView):
    
    model=User
    success_url=reverse_lazy('gmap:list')


class ProUpdate(UpdateView):
    template_name='update.html'
    model=User   
    fields=('name','address','lat','lng','protein','fat','carbohydrate','price','snsimage','openingtime','parking')
    success_url=reverse_lazy('gmap:list')






def index(request):
    template = loader.get_template('gmap/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


class ProCreate(CreateView):
    template_name='gmap/create.html'
    model =Customer
    fields=['name','address','lat','lng','protein','fat','carbohydrate','price','snsimage','openingtime','parking']
    success_url=reverse_lazy('gmap:list')



def listfunc(request):
    object_list  = Customer.objects.all()
    return render(request, 'gmap/list.html', {'object_list':object_list})


def pin(request):
    return render(request, 'gmap/pin.html',{})


def detailfunc(request,pk):
    object=get_object_or_404(Customer,pk=pk)
    return render(request,'gmap/detail.html/',{'object':object})
