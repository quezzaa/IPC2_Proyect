from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Create your views here.

def helloLogin(request):
    return HttpResponse('Bievenido al login')