"""proproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from gmap.models import Customer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('proapp.urls')),
    path('gmap/', include('gmap.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'lat', 'lng')

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gmap/', include('gmap.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('gmap/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]