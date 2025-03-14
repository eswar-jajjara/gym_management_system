# trainers/urls.py
from django.urls import path
from . import views

app_name = 'trainers'  # Namespace for the app

urlpatterns = [
    path('', views.trainers_home, name='trainers'),
]