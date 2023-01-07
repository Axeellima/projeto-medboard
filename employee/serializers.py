from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Employee.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    class Meta:
        model = Employee
        fields = [
        "id",
        "username",
        "password",
        "first_name",
        "last_name",
        "is_superuser",
        "role"
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["is_superuser"]
