from django.db import models


class Contact(models.Model):
    number = models.IntegerField(unique=True)

    employee = models.OneToOneField("Employee", on_delete=models.CASCADE)
    hospital = models.OneToOneField("Hospital", on_delete=models.CASCADE)
    patient = models.OneToOneField("Patient", on_delete=models.CASCADE)
