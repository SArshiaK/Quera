from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.owner == request.user or request.user.is_staff)