from django.db import models


class Consultation(models.Model):
    hospital = models.ForeignKey(
        "hospital.Hospital", on_delete=models.CASCADE, related_name="consults"
    )
    date = models.DateField()
    hour = models.TimeField()
    employee = models.ForeignKey(
        "employee.Employee", on_delete=models.CASCADE, related_name="consults"
    )

    patient = models.ForeignKey(
        "patient.Patient", on_delete=models.CASCADE, related_name="consultation"
    )
