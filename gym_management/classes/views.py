# classes/views.py
from django.shortcuts import render

def classes_home(request):
    return render(request, 'classes/classes_home.html')