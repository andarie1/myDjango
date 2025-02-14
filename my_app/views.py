from django.http import HttpResponse
from django.shortcuts import render

def hello_name(request):
    """Greets me"""
    return HttpResponse("Hello Elena!")
