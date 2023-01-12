from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact = models.OneToOneField(
        "contact.Contact", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.OneToOneField(
        "address.Address", on_delete=models.CASCADE, related_name="hospital", null=True
    )
