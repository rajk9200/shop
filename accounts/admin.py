from django.contrib import admin

# Register your models here.

from .models import Profile,MobileVerification
admin.site.register(Profile)
admin.site.register(MobileVerification)