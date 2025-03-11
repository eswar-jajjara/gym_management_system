from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('user-manual/', views.user_manual, name='user_manual'),
    path('faqs/', views.faqs, name='faqs'),
    path('access-control/', views.access_control, name='access_control'),
    path('contact-support/', views.contact_support, name='contact_support'),  # Add this line
    path('ai-recommendations/', views.ai_recommendations, name='ai_recommendations'),
    path('ai-recommendations-api/', views.ai_recommendations_api, name='ai_recommendations_api'),
]
