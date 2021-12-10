from rest_framework.permissions import BasePermission
from . import Roles


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        client = user.client
        if client.role.name == Roles.CLIENT:
            return True
        return False


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        client = user.client
        if client.role.name == Roles.ADMIN:
            return True
        return False
