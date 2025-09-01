from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, param="Coubeh"):
    return HttpResponse("<h1>Hello " + param +" </h1>")

def contact(request):
    return HttpResponse("<h1>Page Contact Us</h1>")

def about(request):
    return HttpResponse("<h1>Page About Us</h1>")