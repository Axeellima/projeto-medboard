from .models import Employee
from .serializers import EmployeeSerializer, CustomJWTSerializer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status
from django.contrib.auth.hashers import make_password

from roles.models import Role

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from employee.permissions import IsDirectorPermission, IsEmployeeOwnerPermission
from rest_framework_simplejwt.authentication import JWTAuthentication


class EmployeeView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        if self.request.data["role_id"] == "Médico":
            getRole = get_object_or_404(Role, name="Médico")
            serializer.save(
                role=getRole,
                is_staff=True,
                password=make_password(self.request.data["password"]),
            )

        elif self.request.data["role_id"] == "Diretor":
            getRole = get_object_or_404(Role, name="Diretor")
            serializer.save(
                role=getRole,
                is_superuser=True,
                password=make_password(self.request.data["password"]),
            )

        else:
            getRole = get_object_or_404(Role, name="Secretário")
            serializer.save(
                role=getRole, password=make_password(self.request.data["password"])
            )

        return serializer.data


class EmployeeDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsDirectorPermission | IsEmployeeOwnerPermission]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request: Request, pk: int) -> Response:
        employee_obj = get_object_or_404(Employee, id=pk)
        self.check_object_permissions(request, employee_obj)
        serializer = EmployeeSerializer(employee_obj)

        return Response(serializer.data)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
