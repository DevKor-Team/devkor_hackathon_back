from demo.models import DemoImage
from rest_framework import permissions


class IsImageOfMyDemo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: DemoImage):
        if request.user.is_authenticated:
            return obj.demo.team in request.user.teams.all()
        return False

class IsDemoTeamLeader(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.team.leader == request.user
        return False

class IsCommentWriter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.writer == request.user
        return False
