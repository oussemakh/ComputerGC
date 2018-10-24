from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from .forms import FormsignUp
from django.conf import settings
from django.core.mail import send_mail


def signup(request):
    if request.method == 'POST':
        form = FormsignUp(request.POST)
        if form.is_valid():
            user = form.save()
            subject = 'thank you for joining us'
            message = 'welcome to our club we hope you find it use'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']] 
            send_mail(subject,message,email_from,recipient_list)
            login(request, user)
            return redirect('home')

    else:
        form = FormsignUp()
    return render(request, 'signup.html',{'form':form})
    
def LOGIN(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
             user = form.get_user()  
             login(request, user)
             return redirect('home')
            
    else:
         form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def LOGOUT(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('home')