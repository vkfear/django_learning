from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def displayQuote(response):
    return HttpResponse("the best way to make yourself attractive is make couple of goals for next couple of months and work on it")