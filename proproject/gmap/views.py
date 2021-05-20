from .models import Customer
from django.shortcuts import render

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
    template_name='gmap/create.html'
    model =Customer
    fields=['name','address','lat','lng']
    success_url=reverse_lazy('list')



def listfunc(request):
    object_list  = Customer.objects.all()
    return render(request, 'list.html', {'object_list':object_list})