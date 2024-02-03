from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("Request user:", request.user)
        print("Task assigned to:", obj.assigned_to)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.assigned_to == request.user
        