from .models import Employee
from .serializers import EmployeeSerializer

from roles.models import Role

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

import ipdb

class EmployeeView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return self.queryset.filter(role_id=self.request.data["role"])

    def perform_create(self, serializer):
        if(self.request.data["role"] == 2):
            getRole = Role.objects.get_or_create(name="Médico")
            serializer.save(role=getRole[0])

        elif(self.request.data["role"] == 3):
            getRole = Role.objects.get_or_create(name="Diretor")
            serializer.save(role=getRole[0], is_superuser=True)
            
        else:
            getRole = Role.objects.get_or_create(name="Secretário")
            serializer.save(role=getRole[0])

        return serializer.data
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    
class EmployeeDeatilView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer