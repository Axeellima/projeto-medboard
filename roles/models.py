from django.db import models


class RoleName(models.TextChoices):
    SECRETARIO = "Secretário"
    MEDICO = "Médico"
    DIRETOR = "Diretor"


class Role(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=20, choices=RoleName.choices)
