from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from django.conf import settings
from .forms import BuyForm
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url="/nlogin")
def Resrv(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'thank your for using our service'
            message = form.cleaned_data('product_name') + 'thank you for buying it'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, email_from,recipient_list)
            return redirect('home')
           
           
            

    else:
        form = BuyForm()
    return render(request, 'buy.html', {'form':form})
