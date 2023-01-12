from rest_framework import permissions

SECRETARY_METHODS = ("POST", "UPDATE", "DELETE")


class IsSecretaryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SECRETARY_METHODS:
            return True

        return request.user.is_authenticated and not request.user.is_staff


class IsDoctorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsDirectorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
