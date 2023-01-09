from django.db import models


class Consultation(models.Model):
    hospital = models.ForeignKey("hospital.Hospital", on_delete=models.CASCADE, related_name="consults")
    date = models.DateField()
    hour = models.DateTimeField()
    employee = models.OneToOneField("employee.Employee", on_delete=models.CASCADE)

    patient = models.OneToOneField("patient.Patient", on_delete=models.CASCADE)