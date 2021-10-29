from django.shortcuts import render
from django.http import HttpResponse

def getCaptcha(request): 
    print(request)
    return HttpResponse()
