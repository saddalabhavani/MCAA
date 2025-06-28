from django.urls import path
from . import views
urlpatterns = [
   path('insert_student/',views.insert_student, name='insert_student'),
   path('view_student/', views.view_student,  name = 'view_student'),
   path('print-pdf/', views.pdf_view, name='print_pdf'),
]


