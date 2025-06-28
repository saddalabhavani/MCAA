from django.urls import path
from . import views
urlpatterns = [
   path('insert_faculty/',views.insert_faculty, name = 'insert_faculty'),
   path('view_faculty/', views.view_faculty,  name = 'view_faculty'),
   path('delete_faculty/<int:pk>', views.delete_faculty, name = 'delete_faculty'),
   path('update_faculty/<int:pk>', views.update_faculty, name = 'update_faculty'),
   path('print-pdf/', views.pdf_view, name='print_pdf'),
# other paths as needed
]
