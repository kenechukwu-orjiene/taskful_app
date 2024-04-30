from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Create a permission for UserViewset to oly allow user to edit there profile otherwise get or post
    """

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        
        return False
    
class IsProfileOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Create a permission for ProfileViewset to oly allow user to edit there profile otherwise get or post
    """

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user.profile == obj
        
        return False