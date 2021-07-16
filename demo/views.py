from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Demo
from .serializers import DemoSerializer
from .filters import DemoFilter
from .paginations import DemoPagination
from accounts.permissions import IsMyTeam, IsTeamLeader


class DemoViewSet(ModelViewSet):
    pagination_class = DemoPagination
    filterset_class = DemoFilter
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    permission_classes = {
        "list": [],
        "create": [IsTeamLeader | IsAdminUser],
        "retreive": [],
        "update": [IsTeamLeader],
        "destroy": [IsTeamLeader | IsAdminUser],
    }

    def get_permissions(self):
        return [
            permission() for permission in self.permission_classes.get(self.action, [])
        ]
