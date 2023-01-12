from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from employee.permissions import IsPostHospitalPermission, IsDirectorPermission


class HospitalView(APIView):
    queryset = Hospital
    serializer_class = HospitalSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPostHospitalPermission]

    def post(self, req: Request) -> Response:
        serializer = HospitalSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        hospital = Hospital.objects.all()
        serializer = HospitalSerializer(hospital, many=True)

        return Response(serializer.data)


class HospitalDetailView(APIView):
    queryset = Hospital
    serializer_class = HospitalSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsDirectorPermission]

    def patch(self, req: Request, hospital_id: int) -> Response:
        hospital = get_object_or_404(Hospital, id=hospital_id)

        serializer = HospitalSerializer(hospital, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, req: Request, hospital_id: int) -> Response:
        hospital = get_object_or_404(Hospital, id=hospital_id)
        hospital.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
