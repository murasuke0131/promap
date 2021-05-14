from django.shortcuts import render
from .models import ProModel

# Create your views here.

def listfunc(request):
    object_list  = ProModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})