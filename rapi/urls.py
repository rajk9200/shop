from django.urls import path,include

from . import views

from rest_framework import routers

r1 = routers.DefaultRouter()
r1.register('profile',views.ProfileVie)
r1.register('product',views.ProductVie)

urlpatterns =[
    path('api/', include(r1.urls)),
]

