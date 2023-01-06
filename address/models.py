from django.db import models


class Addres(models.Model):
    Street = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    district = models.CharField(max_length=50)
    cep = models.integerField()
