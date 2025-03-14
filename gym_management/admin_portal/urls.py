# admin_portal/urls.py
from django.urls import path
from . import views

app_name = 'admin_portal'  # Namespace for the app

urlpatterns = [
    path('', views.admin_portal_home, name='admin_portal'),
]