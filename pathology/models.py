from django.db import models


class Pathology(models.Model):
    name = models.CharField(max_length=50)

    patient = models.ForeignKey(
        "patient.Patient", on_delete=models.CASCADE, related_name="pathology"
    )
