from django.db import models


CHOOSE_THE_ASSISTANCE = (("Geral", "Geral"), ("Especializada", "Especializada"))

CHOOSE_THE_TYPE = (("Privado", "Privado"), ("Publico", "Publico"))

CHOOSE_FINANCIAL_GOAL = (
    ("Não lucrativo", "Não lucrativo"),
    ("Filantrópico", "Filantrópico"),
    ("Beneficente", "Beneficente"),
)


class Hospital(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type_of_assistance = models.CharField(max_length=50, choices=CHOOSE_THE_ASSISTANCE, null=True)
    type_of_hospital = models.CharField(max_length=50, choices=CHOOSE_THE_TYPE, null=True)
    financial_goal = models.CharField(max_length=50, choices=CHOOSE_FINANCIAL_GOAL, null=True)
    contact = models.OneToOneField("contact.Contact", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
