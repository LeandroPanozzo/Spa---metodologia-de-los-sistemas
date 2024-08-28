from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """
    def has_permission(self, request, view):
        # Solo permite métodos de lectura si no es administrador
        if request.method in permissions.SAFE_METHODS:
            return True
        # Si el usuario es administrador, permite todos los métodos
        return request.user and request.user.is_staff
