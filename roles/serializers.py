from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Role

class RoleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Role.objects.all(),
                message="This role already exists.",
            )
        ],
    )
    class Meta:
        model = Role
        fields = [
        "id",
        "name"
        ]