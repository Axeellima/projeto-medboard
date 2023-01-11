from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ["hospital", "hospital_id", "patient", "patient_id", "data", "hour"]
        depth = 1
        read_only_fields = ["employee"]
        write_only_fields = ["hospital", "patient"]
