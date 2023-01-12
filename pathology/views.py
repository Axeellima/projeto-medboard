from django.shortcuts import render

from .models import Pathology
from .serializers import PathologySerializer

from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from employee.permissions import (
    IsSecretaryPermission,
    IsDoctorPermission,
    IsDirectorPermission,
)


class PathologyView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsDoctorPermission | IsDirectorPermission | IsSecretaryPermission
    ]
    queryset = Pathology.objects.all()
    serializer_class = PathologySerializer
