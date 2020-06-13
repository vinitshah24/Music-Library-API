from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    # To change the error message associated with the exception,
    # implement a message attribute directly on your custom permission.
    message = 'You are already authenticated. Please log out to try again!'

    def has_permission(self, request, view):
        # Check if the user is authenticated
        print("AnonPermissionOnly " + str(request.user))
        return not request.user.is_authenticated


# object-level permissions - run against operations that affect particular obj instance
# Will hide all the important update/delete API methods
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'You must be the owner of this content to modify!'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # SAFE_METHODS -  constant tuple containing 'GET', 'OPTIONS' and 'HEAD'
        print("IsOwnerOrReadOnly " + str(request.user))
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class IsAdminUser(permissions.BasePermission):
    message = 'Superuser Privilege Required!'
    def has_permission(self, request, view):
        print("IsAdminUser " + str(request.user))
        return request.user and request.user.is_superuser
