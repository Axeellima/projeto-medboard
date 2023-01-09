from django.db import models


class Consultation(models.Model):
    hospital = models.ForeignKey("hospitals.Hospital", on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.DateTimeField()
    employee = models.OneToOneField("Employee", on_delete=models.CASCADE)

    patient = models.OneToOneField("Patient", on_delete=models.CASCADE)