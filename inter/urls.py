from inter.views import *
from django.urls import path

urlpatterns=[
    path('mpc/', mpc,name='mpc'),
    path('bpc/',bpc,name='bpc'),
]