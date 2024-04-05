from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello")

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")