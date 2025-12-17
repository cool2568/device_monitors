from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffForWrite(BasePermission):
    """
    - Allow read-only access to authenticated users
    - Allow write access only to staff users
    """

    def has_permission(self,request,view):

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.is_staff
