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

def ai_recommendations(request):
    return render(request, 'ai-recommendations.html')

def generate_workout_plan(goal, fitness_level, equipment):
    workouts = {
        "weight-loss": {
            "beginner": ["Jump Rope (5 mins)", "Bodyweight Squats (3x12)", "Burpees (3x10)"],
            "intermediate": ["Running (30 mins)", "Lunges (3x15)", "Mountain Climbers (3x30)"],
            "advanced": ["HIIT (40 mins)", "Deadlifts (4x8)", "Treadmill Sprints (5x1 min)"]
        },
        "muscle-gain": {
            "beginner": ["Push-ups (3x10)", "Dumbbell Curls (3x12)", "Bodyweight Squats (3x15)"],
            "intermediate": ["Bench Press (4x8)", "Barbell Rows (4x10)", "Pull-ups (3x8)"],
            "advanced": ["Deadlifts (5x5)", "Overhead Press (4x8)", "Weighted Dips (3x10)"]
        }
    }

    return workouts.get(goal, {}).get(fitness_level, ["No plan available"])

@csrf_exempt  # Disable CSRF for testing (Use proper authentication in production)
def ai_recommendations_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            goal = data.get("goal")
            fitness_level = data.get("fitness_level")
            equipment = data.get("equipment")

            workout_plan = generate_workout_plan(goal, fitness_level, equipment)

            return JsonResponse({"success": True, "workout_plan": workout_plan})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
