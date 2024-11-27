from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cse(request):
    return HttpResponse('cse is a branch')
def ece(request):
    return HttpResponse('ece is a electronics brach')
