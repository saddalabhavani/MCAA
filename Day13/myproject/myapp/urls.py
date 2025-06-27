from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
     path('mca101/', views.home, name='mca101'),
     path('mca102/', views.home, name='mca102'),
    ]
