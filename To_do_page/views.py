from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todoGreeting(request):
    return HttpResponse('Hello, this is To-Do Page.')