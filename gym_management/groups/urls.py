# groups/urls.py
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.groups_home, name='groups'),
]