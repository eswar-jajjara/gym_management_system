# supplements/views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Supplement, ProductType, ProductCategory


def supplements_home(request):
    # Get all active supplements
    supplements = Supplement.objects.filter(is_active=True)

    # Get all product types and categories for filters
    types = ProductType.objects.all()
    categories = ProductCategory.objects.all()

    # Get filters from the request
    search_query = request.GET.get('q', '')
    selected_type = request.GET.get('type')
    selected_category = request.GET.get('category')
    weight_goal = request.GET.get('weight_goal')

    # Apply filters
    if search_query:
        supplements = supplements.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if selected_type:
        supplements = supplements.filter(type__id=selected_type)
    if selected_category:
        supplements = supplements.filter(category__id=selected_category)
    if weight_goal:
        supplements = supplements.filter(weight_goal=weight_goal)

    return render(request, 'supplements/supplements_home.html', {
        'supplements': supplements,
        'types': types,
        'categories': categories,
        'search_query': search_query,
        'selected_type': selected_type,
        'selected_category': selected_category,
        'weight_goal': weight_goal,
    })