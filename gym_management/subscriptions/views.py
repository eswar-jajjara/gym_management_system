# subscriptions/views.py
from django.shortcuts import render

def plans(request):
    return render(request, 'plans.html')