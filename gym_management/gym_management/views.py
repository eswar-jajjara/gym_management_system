# gym_management/views.py
from django.shortcuts import render

def book_a_demo(request):
    return render(request, 'book_a_demo.html')