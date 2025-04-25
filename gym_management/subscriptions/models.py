# subscriptions/models.py
from django.db import models


class Plan(models.Model):
    PLAN_TYPES = [
        ('STD', 'Student'),
        ('REG', 'Regular'),
        ('PRM', 'Premium'),
        ('FAM', 'Family'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)  # Default price ₹0
    duration_months = models.PositiveIntegerField(default=1)  # Default 1 month
    benefits = models.TextField(default="No benefits listed")  # Default empty benefits
    plan_type = models.CharField(max_length=3, choices=PLAN_TYPES, default='REG')
    for_men = models.BooleanField(default=True)
    for_women = models.BooleanField(default=True)
    for_students = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} (₹{self.price}/month)"