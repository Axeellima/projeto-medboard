from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Employee(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    role = models.ForeignKey(
        "roles.Role",
        on_delete=models.CASCADE,
        related_name="employees",
        blank=True,
    )