# equipment/urls.py
from django.urls import path
from . import views

app_name = 'equipment'  # Namespace for the app

urlpatterns = [
    path('', views.equipment_home, name='equipment'),
]