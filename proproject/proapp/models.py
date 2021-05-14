from django.db import models

# Create your models here.
class ProModel(models.Model):
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbohydrate = models.IntegerField()
    menu = models.TextField()
    address = models.TextField()
    storename=models.TextField()
    snsimage = models.ImageField(upload_to='')
    price = models.IntegerField()
    openinngtime= models.IntegerField()
    parking=models.BooleanField()
    