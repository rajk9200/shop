from django.urls import path

from . import views

urlpatterns =[
    path('', views.homepage, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_page, name='register'),

]