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

import requests
def opt_generate(mobile,otp_me):


    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "your key", "sender_id": "FSTSMS", "message": otp_me,
                   "language": "english", "route": "p", "numbers": mobile}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response






import random
def mobie_verfication_v(request):
    if request.method=="POST":
        mobilen =request.POST.get('mobilen')
        uotp =request.POST.get('uotp')
        otp =random.randrange(1111,9999)
        otp1 = f"Your Otp Hai {otp}:"
        print(mobilen,otp)
        print(otp1, mobilen)
        # re =opt_generate(mobilen,otp1)
        request.session['mobile']=mobilen
        request.session['otp2']=otp

        return  redirect('verify')

    return render(request, 'loginm.html')

from .models import MobileVerification
def verifiy_otp(request):
    if request.method=="POST":
        uotp =request.POST.get('uotp')
        otp2 =request.session.get('otp2')
        mobile =request.session.get('mobile')

        if(int(uotp)==int(otp2)):
            print('match')
            MobileVerification.objects.create(mobile=mobile, verified=True)
            del request.session['mobile']
            del request.session['otp2']

            return redirect('mreg')
        else:
            print('not match')
    return render(request, 'verify.html')


