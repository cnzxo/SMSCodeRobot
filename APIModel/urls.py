from django.urls import path

import APIModel
from APIModel import views

urlpatterns = [
    path('', APIModel.views.index),
    path('countries/', APIModel.views.countries),
    path('numbers/', APIModel.views.numbers),
    path('numbers/<country>/', APIModel.views.numbers_by_country),
    path('messages/<number>/', APIModel.views.messages_by_number),
]
