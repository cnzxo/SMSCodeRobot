from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('ok')


def countries(request):
    return HttpResponse('ok')


def numbers(request):
    return HttpResponse('ok')
