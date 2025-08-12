from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Careers page")

# Create your views here.
