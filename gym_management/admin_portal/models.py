from django.db import models
from users.models import CustomUser  # Add this if using your CustomUser model

class AuditLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    affected_model = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.action}"