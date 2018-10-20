from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from .forms import FormsignUp

def signup(request):
    if request.method == 'POST':
        form = FormsignUp(request.POST)
        if form.is_valid():
            user = form.save()
           
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