from django.db import models
from django.contrib.auth.models import AbstractUser


class Addres(AbstractUser):
    Street = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    district = models.CharField(max_length=50)
    cep = models.integerField()