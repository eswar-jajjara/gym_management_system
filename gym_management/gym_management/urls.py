# gym_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('membership.urls')),  # Include membership app URLs
    path('subscriptions/', include('subscriptions.urls')),  # Include subscriptions app URLs
    path('users/', include('users.urls')),  # Include users app URLs
    path('subscriptions/', include('subscriptions.urls'))
]