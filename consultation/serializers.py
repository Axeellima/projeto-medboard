from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["all"]
        depth = 1
        
    def create(self, validated_data):
        return Consultation.objects.create(**validated_data)
