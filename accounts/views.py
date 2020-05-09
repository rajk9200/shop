from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register_page(request):
    return render(request, 'registration/register.html')