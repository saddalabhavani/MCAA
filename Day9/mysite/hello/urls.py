from django.urls import path
from .import views

urlpatterns=[
    path('hello/',view.home,name='home'),
]