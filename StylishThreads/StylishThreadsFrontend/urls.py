from django.contrib import admin
from django.urls import path
from StylishThreadsFrontend import views

urlpatterns = [
    path("", views.index, name="StylishThreads"),
]