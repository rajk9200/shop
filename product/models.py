from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from datetime import datetime

class MainCot(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProCot(models.Model):
    main = models.ForeignKey(MainCot,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    # def __str__(self):
    #     return self.name

class Product(models.Model):
    cat =models.ForeignKey(ProCot, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="productImg", default="demo.jpg")
    name = models.CharField(max_length=100)
    price =models.DecimalField(max_digits=8, decimal_places=2)
    desc =models.TextField()
    date = models.DateTimeField(auto_now=True)
    update_date =models.DateTimeField(default=datetime.today)
    ability =models.IntegerField(default=1)
    active =models.BooleanField(default=True)
    slug =models.SlugField(default="-")

    def __str__(self):
        return self.name