from django.shortcuts import render

from .models import Role
from .serializers import RoleSerializer

from rest_framework.generics import CreateAPIView


class RoleView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
