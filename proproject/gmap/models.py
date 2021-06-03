from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=9, decimal_places=7, null=True,blank=True)
    lng = models.DecimalField('経度', max_digits=10, decimal_places=7, null=True,blank=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'