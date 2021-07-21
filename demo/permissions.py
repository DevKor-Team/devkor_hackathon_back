from demo.models import DemoImage
from rest_framework import permissions


class IsImageOfMyDemo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: DemoImage):
        if request.user.is_authenticated:
            return obj.demo.team in request.user.teams.all()
        return False
