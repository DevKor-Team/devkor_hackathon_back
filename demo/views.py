from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import decorators, mixins

from .models import Demo
from .serializers import (
    DemoSerializer,
)
from accounts.permissions import IsMyTeam


class DemoViewSet(ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    permission_classes = {
        "list": [],
        "create": [IsMyTeam | IsAdminUser],
        "retreive": [],
        "update": [IsMyTeam],
        "destroy": [IsMyTeam | IsAdminUser],
    }

    def get_permissions(self):
        return [
            permission() for permission in self.permission_classes.get(self.action, [])
        ]
