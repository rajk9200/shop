from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.decorators import login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def dashboard(request):
    return render(request, 'dashbaord.html')

def register_page(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})