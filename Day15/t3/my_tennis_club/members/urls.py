from django.shortcuts import render
from django.urls import path
from .import views
urlpatterns=[
    path('members/',views.members,name='members')
]

# Create your views here.
