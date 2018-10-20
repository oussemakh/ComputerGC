from django.shortcuts import render
from django.urls import path
from .views import signup, LOGIN, LOGOUT

urlpatterns = [
    path('signup', signup , name="signup"),
    path('login', LOGIN, name="login"),
    path('logout', LOGOUT, name="logout"),
]
