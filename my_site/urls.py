from django.contrib import admin
from django.urls import path
from forms_app.views import feedback_view, dashboard_view, export_excel, edit_feedback, delete_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedback_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'), 
    path('export/', export_excel, name='export_excel'), 
    path('dashboard/edit/<int:pk>/', edit_feedback, name='edit_feedback'),
    path('dashboard/delete/<int:pk>/', delete_feedback, name='delete_feedback'),
]