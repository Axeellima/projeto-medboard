from rest_framework import serializers

from pathology.serializers import PathologySerializer
from pathology.models import Pathology
from .models import Patient
from .utils import generatePatientCode, generatePatientPassword
import ipdb


class PatientSerializer(serializers.ModelSerializer):
    pathology = PathologySerializer(many=True)

    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "birth_date",
            "patient_code",
            "contact",
            "pathology",
        ]
        read_only_fields = ["patient_code", "password"]

    def create(self, validated_data: dict) -> Patient:
        pathology_list = validated_data.pop("pathology")
        # ipdb.set_trace()
        patient_code = generatePatientCode()
        patient_password = generatePatientPassword()

        patient_obj = Patient.objects.create(
            **validated_data,
            patient_code=patient_code,
            password=patient_password,
        )

        for pathology_dict in pathology_list:
            pathology_obj, create = Pathology.objects.get_or_create(**pathology_dict)
            patient_obj.pathology.add(pathology_obj)

        patient_obj.save()
        return patient_obj

    def update(self, instance: Patient, validated_data: dict) -> Patient:
        pathology_list = validated_data.pop("pathology")

        pathology_update = []
        for pathology_item in pathology_list:
            if pathology_item:
                pathology_obj = Pathology.objects.filter(name=pathology_item["name"])[0]
                pathology_update.append(pathology_obj)

        if len(pathology_update) > 0:
            instance.pathology.set(pathology_update)

        instance.save()
        return instance
