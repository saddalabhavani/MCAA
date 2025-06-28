from django.urls import path
from .import views

urlspatterns=[
    path('members/',views.members, name='members'),
]