from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from .forms import BuyForm

# Create your views here.
@login_required(login_url="/nlogin")
def Resrv(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            username =user['username']
            email = user['email']
            password = user['password']
            if not(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):

                User.objects.create_user(username, email,password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
           
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

            

    else:
        form = BuyForm()
    return render(request, 'buy.html', {'form':form})
