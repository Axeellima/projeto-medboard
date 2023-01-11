from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer

class HospitalView(APIView):

    def get(self, req: Request) -> Response:
        hospital = Hospital.objects.all()
        serializer = HospitalSerializer(hospital, many = True)

        return Response(serializer.data)

class HospitalDetailView(APIView):

    def patch(self, req: Request, hospital_id: int) -> Response:
        hospital = get_object_or_404(Hospital, id=hospital_id)

        serializer = HospitalSerializer(hospital, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete (self, req: Request, hospital_id: int) -> Response:
        hospital = get_object_or_404(Hospital, id=hospital_id)
        hospital.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class HospitalCreateView(APIView):

    def post (self, req: Request) -> Response:
        serializer = HospitalSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)