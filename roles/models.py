from django.db import models

CHOOSE_ROLE_NAME = (
    ("Secretário", "Secretário"),
    ("Médico", "Médico"),
    ("Diretor", "Diretor"),
)


class Role(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=20, choices=CHOOSE_ROLE_NAME)
