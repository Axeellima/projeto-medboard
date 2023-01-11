from .models import Employee
from .serializers import EmployeeSerializer

from django.shortcuts import get_object_or_404

from roles.models import Role

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class EmployeeView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):

        if(self.request.data["role_id"] == 2):
            getRole = get_object_or_404(Role, id=2)
            serializer.save(role=getRole)

        elif(self.request.data["role_id"] == 3):
            getRole = get_object_or_404(Role, id=3)
            serializer.save(role=getRole, is_superuser=True)
            
        else:
            getRole = get_object_or_404(Role, id=1)
            serializer.save(role=getRole)

        return serializer.data
    
class EmployeeDetailView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer