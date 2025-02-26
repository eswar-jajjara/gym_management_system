# subscriptions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans, name='plans'),  # Plans page URL
]