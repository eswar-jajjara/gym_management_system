# groups/views.py
from django.shortcuts import render

def groups_home(request):
    # Dummy data for groups (replace with database queries later)
    groups = [
        {
            'name': 'Muscle Gain Group',
            'description': 'A group for members focusing on muscle building.',
            'members': 120,
        },
        {
            'name': 'Weight Loss Group',
            'description': 'A group for members focusing on weight loss.',
            'members': 95,
        },
    ]
    return render(request, 'groups/groups_home.html', {'groups': groups})