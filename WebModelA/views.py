from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def countries(request):
    return render(request, 'countries.html')


def numbers(request):
    return render(request, 'numbers.html')