from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    district = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=9)
