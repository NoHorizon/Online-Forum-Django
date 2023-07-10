from django.shortcuts import render

#custom
from django.http import HttpResponse

# Create your views here.
#custom

def home(request): #custom
    return HttpResponse('Home Page, this text(function) location base/views.py"')

def room(request): #custom
    return HttpResponse("ROOM, this text(function) location base/views.py")
