from rest_framework import permissions

class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted

class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-authenticated users only
    """
    message = "You are already authenticated. Please log out to try again."
    def has_permission(self, request, view):
        return not request.user.is_authenticated()

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows Admin users to POST and anonymous to GET
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # User must be Administrator    
        return request.user.is_staff

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = "You must be the owner of this content to change."
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user

class IsEnrolled(permissions.BasePermission):
    message = "You need to be authorized to continue. Please enroll to the course first."
    def has_permission(self, request, view):
        enrolled = Courses.objects.get(user=request.user).exists()
        return enrolled