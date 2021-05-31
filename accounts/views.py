from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework import mixins

from accounts.models import User, Profile, Team
from accounts.serializers import (
    UserSerializer,
    ProfileSerializer,
    TeamSerializer,
    TeamTokenSerializer,
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
    }

    def get_permissions(self):
        return [
            permission() for permission in self.permission_classes.get(self.action, [])
        ]


class MeView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class MyTeamView(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamTokenSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.get_serializer(request.user.teams, many=True)
        return Response(serializer.data)
