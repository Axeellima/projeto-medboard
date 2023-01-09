from rest_framework import serializers
from rest_framework import UniqueValidator

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(
        validators=[
            UniqueValidator(
                queryset=Contact.objects.all(),
                message="This contact already exists.",
            )
        ],
    )
