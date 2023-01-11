from django.db import models


class Contact(models.Model):
    number = models.IntegerField(unique=True)
