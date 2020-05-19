from django.db import models

class Profile(models.Model):
    mobile = models.CharField(max_length=10)
    name =models.CharField(max_length=100)



class MobileVerification(models.Model):
    mobile = models.CharField(max_length=10)
    verified =models.BooleanField(default=False)
