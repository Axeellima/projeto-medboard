from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from contact.serializers import ContactSerializer
from contact.models import Contact

from .models import Employee
from roles.models import Role, RoleName


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("get_token do employee", user)
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        token["is_staff"] = user.is_staff
        return token


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Employee.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    role_id = serializers.ChoiceField(choices=RoleName.choices)
    contact = ContactSerializer()

    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "role_id",
            "contact",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["is_superuser"]
        write_only_fields = ["role_id"]

    def create(self, validated_data: dict) -> Employee:
        role_data = validated_data.pop("role_id")
        role = Role.objects.get(name=role_data)
        role_id = role.id

        contact_data = validated_data.pop("contact")
        contatct_obj = Contact.objects.create(**contact_data)

        employee_obj = Employee.objects.create(
            **validated_data, contact=contatct_obj, role_id=role_id
        )
        employee_obj.save()

        return employee_obj
