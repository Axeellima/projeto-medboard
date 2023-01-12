from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Role, CHOOSE_ROLE_NAME


class RoleSerializer(serializers.ModelSerializer):
    name = serializers.ChoiceField(
        validators=[
            UniqueValidator(
                queryset=Role.objects.all(),
                message="This role already exists.",
            )
        ],
        choices=CHOOSE_ROLE_NAME,
    )

    class Meta:
        model = Role
        fields = ["id", "name"]
