from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    patient_code = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    
    contact = models.OneToOneField("contact.Contact", on_delete=models.CASCADE, null=True)