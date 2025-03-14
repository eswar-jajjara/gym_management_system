# gym_management/urls.py
from django.contrib import admin
from django.urls import path, include
from membership import views  # Import views from the membership app

urlpatterns = [
    path('subscriptions/', include('subscriptions.urls')),
    path('users/', include('users.urls')),
    path('', include('membership.urls')),  # Root URL should be last
    path('admin/', admin.site.urls),
    path('classes/', include('classes.urls')),
    path('trainers/', include('trainers.urls')),
    path('schedule/', include('schedule.urls')),
    path('admin-portal/', include('admin_portal.urls')),
    path('supplements/', include('supplements.urls')),
    path('equipment/', include('equipment.urls')),
    path('groups/', include('groups.urls')),
    path('book-a-demo/', views.book_a_demo, name='book_a_demo'),  # Use the imported views
]