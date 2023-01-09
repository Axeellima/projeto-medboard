from django.db import models


class Contact(models.Model):
    number = models.IntegerField(unique=True)

    employee = models.OneToOneField("employee.Employee", on_delete=models.CASCADE)
    hospital = models.OneToOneField("hospital.Hospital", on_delete=models.CASCADE)
    patient = models.OneToOneField("patient.Patient", on_delete=models.CASCADE)
