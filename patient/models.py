from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    patient_code = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=10, null=True)

    contact = models.OneToOneField(
        "contact.Contact", on_delete=models.CASCADE, null=True
    )
    pathology = models.ManyToManyField(
        "pathology.Pathology",
        related_name="patient",
    )
