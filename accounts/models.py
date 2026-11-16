from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    enrolled_course = models.CharField(
        max_length=100
    )

    section = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_id})"
