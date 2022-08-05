from django.urls import path

import WebModel
from WebModel import views

urlpatterns = [
    path('', WebModel.views.index),
    path('countries/', WebModel.views.countries),
    path('numbers/', WebModel.views.numbers),
    path('messages/', WebModel.views.messages),
    path('documents/', WebModel.views.documents),
    path('privacy/', WebModel.views.privacy),
]
