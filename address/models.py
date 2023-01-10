from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    district = models.CharField(max_length=50)
    cep = models.IntegerField()

    hospital = models.OneToOneField(
        "hospital.Hospital", on_delete=models.CASCADE, related_name="address"
    )
