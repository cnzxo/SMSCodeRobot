from django.urls import path

import APIModelA
from APIModelA import views

urlpatterns = [
    path('', APIModelA.views.index),
    path('countries/', APIModelA.views.countries),
    path('numbers/', APIModelA.views.numbers),
    path('numbers/<country>/', APIModelA.views.numbers_by_country),
    path('messages/<number>/', APIModelA.views.messages_by_number),
]
