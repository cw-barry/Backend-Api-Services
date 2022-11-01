from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "You must be the owner of this post"

    # def has_object_permission(self, request, obj):
    #     return obj.author == request.user

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author == request.user
