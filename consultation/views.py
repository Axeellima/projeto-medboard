from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response, Request, status

from .models import Consultation
from .serializers import ConsultationSerializer
from .utils import checkConsultationDate
from hospital.models import Hospital
from patient.models import Patient

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from employee.permissions import IsDoctorPermission, IsDirectorPermission

from django.http import HttpResponseBadRequest


class ConsultationView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsDoctorPermission | IsDirectorPermission]
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

    def perform_create(self, serializer):
        if checkConsultationDate(self.request.data):
            hospital_id = self.request.data["hospital_id"]
            hospital = get_object_or_404(Hospital, id=hospital_id)

            patient_id = self.request.data["patient_id"]
            patient = get_object_or_404(Patient, id=patient_id)

            consultation_list = Consultation.objects.all().filter(
                employee_id=self.request.user.id
            )
            side_list = []
            for consultation_dict in consultation_list:
                if str(consultation_dict.date) == str(
                    self.request.data["date"]
                ) and str(consultation_dict.hour)[0:5] == str(
                    self.request.data["hour"]
                ):
                    side_list.append(consultation_dict)
            if len(side_list) > 0:
                raise ValueError("Consultation already exists")

            serializer.save(
                employee=self.request.user, hospital=hospital, patient=patient
            )

            return serializer.data

        raise ValueError("Invalid date")


class ConsultationDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsDoctorPermission | IsDirectorPermission]
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
