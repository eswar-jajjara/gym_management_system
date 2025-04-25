# equipment/views.py
from django.shortcuts import render

def equipment_home(request):
    # Dummy data for demonstration
    equipment = [
        {'name': 'Treadmill', 'category': 'Cardio', 'price': 49999, 'image': 'images/treadmill.jpg', 'description': 'High-end treadmill for home workouts.'},
        {'name': 'Dumbbell Set', 'category': 'Weights', 'price': 7999, 'image': 'images/dumbbell_set.jpg', 'description': 'Adjustable dumbbell set for strength training.'},
    ]
    return render(request, 'equipment/equipment_home.html', {'equipment': equipment})