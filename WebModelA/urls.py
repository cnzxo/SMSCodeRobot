from django.urls import path

import WebModelA
from WebModelA import views

urlpatterns = [
    path('', WebModelA.views.index),
    path('countries/', WebModelA.views.countries),
    path('numbers/', WebModelA.views.numbers),
]