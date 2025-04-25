# schedule/models.py
from django.db import models
from users.models import CustomUser


class ScheduleSlot(models.Model):
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'TRAINER'})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField(default=10)
    booked_members = models.ManyToManyField(CustomUser, related_name='booked_slots', blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_time__gt=models.F('start_time')),
                name="end_after_start"
            )
        ]