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