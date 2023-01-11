from rest_framework import serializers
from hospital.models import Hospital
from address.models import Address
from address.serializers import AddressSerializer
from hospital.models import (
    CHOOSE_FINANCIAL_GOAL,
    CHOOSE_THE_ASSISTANCE,
    CHOOSE_THE_TYPE,
)


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ["id", "name", "type_of_assistance", "type_of_hospital", "financial_goal", "created_at", "updated_at", "address"]
        read_only_fields= ["created_at", "updated_at"]

    def create(self,validated_data:dict) -> Hospital:
        address_list = validated_data.pop('address')
        hospitalobj = Hospital.objects.create(**validated_data)
        
        for address_dict in address_list:
            addressobj, created = Address.objects.get_or_create(**address_dict)

            hospitalobj.address.add(addressobj)
        
        return hospitalobj
    
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
