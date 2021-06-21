from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework import decorators, mixins

from accounts.models import User, Profile, Team
from accounts.serializers import (
    UserSerializer,
    ProfileSerializer,
    TeamSerializer,
)
from accounts.permissions import IsMyTeam


class ProfileViewSet(GenericViewSet, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = {
        "list": [],
        "create": [IsAdminUser],
        "retreive": [],
        "update": [IsMyTeam],
        "destroy": [IsAdminUser],
        "token": [IsMyTeam, IsAdminUser],
        "register": [IsAuthenticated],
        "leave": [IsMyTeam],
    }

    def get_permissions(self):
        return [
            permission() for permission in self.permission_classes.get(self.action, [])
        ]

    @decorators.action(methods=["GET"], detail=True)
    def token(self, request):  # celery로 주기적 업데이트?
        team = self.get_object()
        team.create_token()
        return Response({"token": team.token})

    @decorators.action(methods=["POST"], detail=True)
    def register(self, request):
        team = self.get_object()
        token = request.data.get("token")

        success = team.verify_token(token)

        if success:
            request.user.teams.add(team)

        return Response({"success": success})

    @decorators.action(methods=["POST"], detail=True)
    def leave(self, request):
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
