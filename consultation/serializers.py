from rest_framework import serializers
from .models import Consultation


class ConsultationSerializer(serializers.ModelSerializer):
    hospital_id = serializers.IntegerField()
    patient_id = serializers.IntegerField()

    class Meta:
        model = Consultation
        fields = ["hospital", "hospital_id", "patient_id", "date", "hour"]
        depth = 1
        read_only_fields = ["employee", "hospital", "patient"]
        write_only_fields = ["hospital_id", "patient_id"]
