# supplements/urls.py
from django.urls import path
from . import views

app_name = 'supplements'  # Namespace for the app

urlpatterns = [
    path('', views.supplements_home, name='supplements'),
]