from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow World")

# Create your views here.
