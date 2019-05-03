from rest_framework.permissions import BasePermission


class CarOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Доступ у хозяина авто"""
        return obj.owner == request.user
