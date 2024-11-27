from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mpc(request):
    return HttpResponse('mpc  means maths, pysics, chemistry')
def bpc(request):
    return HttpResponse('bpc  means biology, pysics ,chemistry')
