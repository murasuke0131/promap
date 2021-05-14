from django.shortcuts import render

# Create your views here.

def createfunc(request):
    if request.method == "POST":
        address = request.POST['address']
        price = request.POST['price']
    return render(request, 'create.html', {})