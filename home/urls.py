
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('allpro/', views.allProduct, name='allpro'),
    path('allCat/', views.allCategery, name='allCat'),
    # path('checkout/', views.checkout, name='checkout'),
]
