from btech.views import*
from django.urls import path

urlpatterns=[
    path('cse/', cse,name='cse'),
    path('ece/',ece,name='ece'),
]