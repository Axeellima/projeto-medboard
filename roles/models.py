from django.db import models

# Create your models here.
class Role(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=20)