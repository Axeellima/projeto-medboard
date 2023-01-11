from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer

class HospitalDetailView(APIView):
    def patch(self, req: Request, hospital_id: int) -> Response:
        hospital = get_object_or_404(Hospital, id=hospital_id)

        serializer = HospitalSerializer(hospital, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
