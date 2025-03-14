# classes/urls.py
from django.urls import path
from . import views

app_name = 'classes'  # Namespace for the app

urlpatterns = [
    path('', views.classes_home, name='classes'),
]