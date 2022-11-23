from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    return HttpResponse("<h1>first django app</h1>")

def displaydatetime(request):
    dt=datetime.datetime.now()
    s = "<b>Current date and time: </b>"+str(dt)
    return HttpResponse(s)