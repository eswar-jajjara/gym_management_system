# trainers/views.py
from django.shortcuts import render

def trainers_home(request):
    # Dummy data for demonstration
    trainers = [
        {'name': 'John Doe', 'expertise': 'Strength Training', 'image': 'images/trainer1.jpg'},
        {'name': 'Jane Smith', 'expertise': 'Yoga', 'image': 'images/trainer2.jpg'},
    ]
    return render(request, 'trainers/trainers_home.html', {'trainers': trainers})