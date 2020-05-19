from django.contrib import admin

# Register your models here.
from .models import ProCot,Product,MainCot,Cart
admin.site.register(MainCot)
admin.site.register(ProCot)
admin.site.register(Product)
admin.site.register(Cart)