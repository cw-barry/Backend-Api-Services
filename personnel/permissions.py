from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        allow = bool(request.user and request.user.is_staff) # True or False
        return allow