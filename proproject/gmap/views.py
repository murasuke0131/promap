from .models import Customer
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from .models import Customer
from django.urls import reverse_lazy


def index(request):
    template = loader.get_template('gmap/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


class ProCreate(CreateView):
    template_name='gmap/pin.html'
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
    return render(request,'detail.html',{'object':object})
