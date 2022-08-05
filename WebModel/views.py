import uuid
from django.shortcuts import render

mac = "-".join([uuid.UUID(int=uuid.getnode()).hex[-12:][e:e + 2] for e in range(0, 11, 2)]).upper()


# Create your views here.
def index(request):
    return render(request, 'index.html', {'node': '{}:{}'.format(mac, request.META['SERVER_PORT'])})


def countries(request):
    return render(request, 'countries.html', {'node': '{}:{}'.format(mac, request.META['SERVER_PORT'])})


def numbers(request):
    return render(request, 'numbers.html', {'node': '{}:{}'.format(mac, request.META['SERVER_PORT'])})


def messages(request):
    return render(request, 'messages.html', {'node': '{}:{}'.format(mac, request.META['SERVER_PORT'])})


def documents(request):
    return render(request, 'documents.html', {'node': '{}:{}'.format(mac, request.META['SERVER_PORT'])})


def privacy(request):
    return render(request, 'privacy.html', {'node': '{}:{}'.format(mac, request.META['SERVER_PORT'])})
