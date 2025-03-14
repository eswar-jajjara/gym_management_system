import json  # Required for handling JSON requests
from django.http import JsonResponse  # Required for returning JSON responses
from django.views.decorators.csrf import csrf_exempt  # Required for @csrf_exempt
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def support(request):
    return render(request, 'support.html')

def user_manual(request):
    return render(request, 'user_manual.html')  # Ensure 'user_manual.html' exists in templates

def faqs(request):
    return render(request, 'faqs.html')

def access_control(request):
    return render(request, 'access_control.html')

def contact_support(request):
    return render(request, 'contact_support.html')

def gym_ai(request):
    return render(request, 'gym_ai.html')  # If the template is in 'templates/' directly


def book_a_demo(request):
    return render(request, 'book_a_demo.html')