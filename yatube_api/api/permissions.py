from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """A class that defines that only the author can make changes."""
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user == obj.author
