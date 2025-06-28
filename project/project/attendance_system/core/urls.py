from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.student_list,name='core_home'),  # Add this line
    path('student_list/', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('report/', views.attendance_report, name='attendance_report'),
]
