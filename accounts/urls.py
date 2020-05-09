from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns =[
    path('', views.homepage, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_page, name='register'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),

]

