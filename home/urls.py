
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('allpro/', views.allProduct, name='allpro'),
    path('allCat/', views.allCategery, name='allCat'),
    path('product=<str:slug>/', views.details_view, name='details'),
    path('checkout/', views.checkout, name='checkout'),
]
