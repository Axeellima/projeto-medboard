import random, string

from rest_framework import serializers

from pathology.serializer import PathologySerializer
from pathology.models import Pathology
from .models import Patient


class PatientSerializar(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ["id", "name", "birth_date", "patient_code", "password", "contact"]
        read_only_fields = ["patient_code", "password"]


    def generatePatientCode():
        letters = string.ascii_uppercase
        random_string = "".join(random.choice(letters) for i in range(4))

        random_number = random.random()
        round_number = round((random_number * 10000))

        patient_code = f"{random_string}{round_number}"
        return patient_code

    def generatePatientPassword():
        random_number = random.random()
        password = round((random_number * 1000000))

        return password

    def create(self, validated_data: dict) -> Patient:
        pathology_list = validated_data.pop("pathology")

        patient_code = self.generatePatientCode()
        patient_password = self.generatePatientPassword()

        patient_obj, create = Patient.objects.create(
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
