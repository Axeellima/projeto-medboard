from django.shortcuts import render

# Create your views here.
from .models import Role

from .serializers import RoleSerializer

from rest_framework.generics import CreateAPIView

class RoleView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer