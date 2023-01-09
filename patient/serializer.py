from rest_framework import serializers
from pathology.serializer import PathologySerializer


class PatientSerializar(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    patient_code = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=10)

    pathology = PathologySerializer()
