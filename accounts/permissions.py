from rest_framework import permissions


class IsMyTeam(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj in request.user.teams.all()
        return False

class IsTeamLeader(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj == request.user.teams.leader
        return False

