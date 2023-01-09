from rest_framework import serializers
from hospital.models import Hospital
from address.models import Address
from address.serializers import AddressSerializer
from hospital.models import (
    CHOOSE_FINANCIAL_GOAL,
    CHOOSE_THE_ASSISTANCE,
    CHOOSE_THE_TYPE,
)


class HospitalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, unique=True)
    type_of_assistance = serializers.ChoiceField(choices=CHOOSE_THE_ASSISTANCE, allow_null=True)
    type_of_hospital = serializers.ChoiceField(choices=CHOOSE_THE_TYPE, allow_null=True)
    financial_goal = serializers.ChoiceField(choices=CHOOSE_FINANCIAL_GOAL, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    address = AddressSerializer()
    
    def update(self, instance: Hospital, validated_data: dict):
        address_dict: dict = validated_data.pop("address", None)
        
        if address_dict:
            address_obj, created = Address.objects.get_or_create(user=instance)
            for key, value in address_dict.items():
                setattr(address_obj, key, value)
            address_obj.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
