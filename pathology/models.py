from django.db import models


class Pathology(models.Model):
    name = models.CharField(max_length=50)
