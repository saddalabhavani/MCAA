from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee, name = 'insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
   path('delete_employee/<int:pk>', views.delete_employee, name = 'delete_employee'),
   path('update_employee/<int:pk>', views.update_employee, name = 'update_employee'),
]