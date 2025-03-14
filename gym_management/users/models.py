from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('MEMBER', 'Member'),
        ('TRAINER', 'Trainer'),
        ('ADMIN', 'Admin'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='MEMBER')
    membership_type = models.CharField(max_length=20, blank=True)
    assigned_trainer = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )

    # Fix conflicts with Django's default User model
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Change from 'user_set' to 'customuser_set'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",  # Change from 'user_set' to 'customuser_permissions_set'
        blank=True
    )
