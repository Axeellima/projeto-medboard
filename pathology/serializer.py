from rest_framework import serializers
from .models import Pathology


class PathologySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        pathology_obj, create = Pathology.objects.create(**validated_data)
        if create:
            return pathology_obj
