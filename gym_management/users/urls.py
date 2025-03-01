# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),  # Your existing login view
    path('register/', views.register, name='register'),  # Add this line
]