from rest_framework import serializers
from hospital.models import Hospital
from address.models import Address
from address.serializers import AddressSerializer
import ipdb


class HospitalSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Hospital
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
            "address",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data: dict) -> Hospital:
        address_dict = validated_data.pop("address")
        addressobj, created = Address.objects.get_or_create(**address_dict)

        hospitalobj = Hospital.objects.create(**validated_data, address=addressobj)

        hospitalobj.save()
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
