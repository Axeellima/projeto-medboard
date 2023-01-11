from rest_framework import serializers
from .models import Pathology


class PathologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pathology
        fields = ["id", "name", "patient"]

    def create(self, validated_data):
        pathology_obj, create = Pathology.objects.create(**validated_data)
        if create:
            return pathology_obj
