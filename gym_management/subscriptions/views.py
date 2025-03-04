from django.shortcuts import render
from .models import Plan

def pricing(request):
    plans = Plan.objects.all()
    print(plans)  # Debug: Check terminal output
    return render(request, 'pricing.html', {'plans': plans})