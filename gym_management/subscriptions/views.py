# subscriptions/views.py
from django.shortcuts import render
from .models import Plan

def pricing(request):
    plans = Plan.objects.all()
    print("Plans found:", list(plans))  # Debug output
    return render(request, 'pricing.html', {'plans': plans})