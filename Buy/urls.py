from django.urls import path,include
from .views import Resrv
urlpatterns = [
    path('resv', Resrv , name="buy"),
]
