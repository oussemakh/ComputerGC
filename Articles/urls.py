
from django.urls import path
from django.conf.urls import url

from .views import home,detail

urlpatterns = [
    path('', home, name="home"),
    url(r'^(?P<slug1>[-\w]+)/$', detail, name='article_detail'),
    
]
