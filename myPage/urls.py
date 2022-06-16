from django.urls import path

from . import views

URLPatterns = [
    path("",views.index),
]