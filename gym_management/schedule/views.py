# schedule/views.py
from django.shortcuts import render

def schedule_home(request):
    # Dummy data for demonstration
    schedule_slots = [
        {'name': 'Morning Yoga', 'time': '6:00 AM - 7:00 AM', 'trainer': 'Jane Smith'},
        {'name': 'Evening Strength Training', 'time': '6:00 PM - 7:00 PM', 'trainer': 'John Doe'},
    ]
    return render(request, 'schedule/schedule_home.html', {'schedule_slots': schedule_slots})