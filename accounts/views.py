from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import decorators, mixins

from devathon.viewsets import ActionModelViewSet

from accounts.models import User, Profile, Team
from accounts.serializers import (
    UserSerializer,
    ProfileSerializer,
    TeamSerializer,
)
from accounts.permissions import IsMyTeam, IsMyProfile


class ProfileViewSet(GenericViewSet, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TeamViewSet(ActionModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    action_permission_classes = {
        "list": [],
        "create": [IsAdminUser],
        "retreive": [],
        "partial_update": [IsMyTeam],
        "update": [IsMyTeam],
        "destroy": [IsAdminUser],
        "token": [IsMyTeam | IsAdminUser],
        "register": [IsAuthenticated],
        "leave": [IsMyTeam],
    }

    @decorators.action(methods=["GET"], detail=True)
    def token(self, request, pk=None):
        team = self.get_object()
        token = team.create_token()
        return Response({"token": token})

    @decorators.action(methods=["POST"], detail=True)
    def register(self, request, pk=None):
        team = self.get_object()
        token = request.data.get("token")

        success = team.verify_token(token)

        if success:
            request.user.teams.add(team)

        return Response({"success": success})

    @decorators.action(methods=["POST"], detail=True)
    def leave(self, request, pk=None):
        try:
            request.user.teams.remove(self.get_object())
            return Response({"success": True})
        except:
            return Response({"success": False})


class MeView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class MyTeamView(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user.teams, many=True)
        return Response(serializer.data)
