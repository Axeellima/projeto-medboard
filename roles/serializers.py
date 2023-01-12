from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Role, RoleName


class RoleSerializer(serializers.ModelSerializer):
    name = serializers.ChoiceField(
        validators=[
            UniqueValidator(
                queryset=Role.objects.all(),
                message="This role already exists.",
            )
        ],
        choices=RoleName.choices,
    )

    class Meta:
        model = Role
        fields = ["id", "name"]
