from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField('店名', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=10, decimal_places=7, null=True,blank=True)
    lng = models.DecimalField('経度', max_digits=10, decimal_places=7, null=True,blank=True)
    protein =models.DecimalField ('タンパク質',max_digits=4,decimal_places=1,null=True,blank=True)
    fat = models.DecimalField('脂質',max_digits=4,decimal_places=1,null=True,blank=True)
    carbohydrate =models.DecimalField ('炭水化物',max_digits=4,decimal_places=1,null=True,blank=True)
    menu = models.TextField('メニュー',null=True,blank=True)
    snsimage = models.ImageField('写真',upload_to='',null=True,blank=True)
    price = models.IntegerField('値段',null=True,blank=True)
    openingtime= models.IntegerField('営業時間',null=True,blank=True)
    parking=models.BooleanField('駐車場',null=True,blank=True)
    


    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'