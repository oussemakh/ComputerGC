from django.urls import path
from django.conf.urls import url 
from .views import see_learn, learn_detail

urlpatterns = [
    path('see&learn', see_learn, name="slearn"),
    url(r'^(?P<slug2>[-\w]+)/men$', learn_detail, name="learn-detail"),
]
