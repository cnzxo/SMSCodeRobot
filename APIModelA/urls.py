from django.urls import path

import APIModelA
from APIModelA import views

urlpatterns = [
    path('', APIModelA.views.index),
    path('countries/', APIModelA.views.countries),
    path('numbers/', APIModelA.views.numbers),
]
