from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """ Права доступа: только создатель или чтение """
    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user == obj.user
        return request.user.is_authenticated and request.user == obj.user
