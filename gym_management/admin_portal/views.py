from django.shortcuts import render

def admin_portal_home(request):
    return render(request, 'admin_portal/home.html')  # Ensure this template exists
