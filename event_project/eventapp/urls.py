from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/add/', views.event_create, name='event_create'),
    path('event/edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('event/delete/<int:pk>/', views.event_delete, name='event_delete'),

    path('register/', views.register_participant, name='register_participant'),
    path('registrations/', views.registration_list, name='registration_list'),
    path('report/', views.registration_report, name='registration_report'),

]
