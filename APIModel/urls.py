from django.urls import path

import APIModel
from APIModel import views

urlpatterns = [
    path('', APIModel.views.index),
    path('countries/', APIModel.views.countries),
    path('numbers/', APIModel.views.numbers),
    path('info/', APIModel.views.info),
]
