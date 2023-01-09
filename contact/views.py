from django.shortcuts import render


from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Contact
from .serializers import ContactSerializer


class ContactView(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
