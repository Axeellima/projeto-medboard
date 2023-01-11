from django.shortcuts import render

from .models import Consultation
from .serializers import ConsultationSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ConsultationView(ListCreateAPIView):

    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

    def perform_create(self, serializer):

        
        
        serializer.save(employee=self.request.user)

        return serializer.data


class ConsultationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer