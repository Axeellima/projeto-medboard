from rest_framework import serializers
from .models import Pathology


class PathologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathology
        fields = ["id", "name"]
