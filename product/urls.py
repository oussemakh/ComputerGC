from django.urls import path,include
from django.conf.urls import url
from .views import product, productd

urlpatterns = [

    path('product', product , name="product"),
    url(r'^(?P<slug>[\w.@+-]+)/info$', productd, name='product-detail'),
    
]