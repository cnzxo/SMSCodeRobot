import re
import time

# Create your views here.
from bs4 import BeautifulSoup
from django.shortcuts import render

from APIModel.common import http_request_get


def index(request):

    return render(request, 'index.html')
