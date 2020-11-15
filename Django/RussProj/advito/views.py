from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def marketplace(request):
    return HttpResponse('Hello, Advito')
