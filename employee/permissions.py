from rest_framework import permissions


class IsDoctorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == "Médico"


class IsSecretaryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == "Secretário"
