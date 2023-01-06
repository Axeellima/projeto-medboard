from django.db import models
from django.contrib.auth.models import AbstractUser


CHOOSE_THE_ASSISTANCE = (("Geral", "Geral"), ("Especializada", "Especializada"))

CHOOSE_THE_TYPE = (("Privado", "Privado"), ("Publico", "Publico"))

CHOOSE_FINANCIAL_GOAL = (
    ("Não lucrativo", "Não lucrativo"),
    ("Filantrópico", "Filantrópico"),
    ("Beneficente", "Beneficente"),
)


class Hospital(AbstractUser):
    name = models.CharField(max_length=50, unique=True)
    type_of_assistance = models.CharField(max_length=50, choices=CHOOSE_THE_ASSISTANCE)
    type_of_hospital = models.CharField(max_length=50, choices=CHOOSE_THE_TYPE)
    financial_goal = models.CharField(max_length=50, choices=CHOOSE_FINANCIAL_GOAL)


class Addres(AbstractUser):
    Street = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    district = models.CharField(max_length=50)
    cep = models.integerField()
