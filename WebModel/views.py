# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def countries(request):
    return render(request, 'countries.html')


def numbers(request):
    return render(request, 'numbers.html')
