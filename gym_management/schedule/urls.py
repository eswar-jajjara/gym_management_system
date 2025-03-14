# schedule/urls.py
from django.urls import path
from . import views

app_name = 'schedule'  # Namespace for the app

urlpatterns = [
    path('', views.schedule_home, name='schedule'),
]