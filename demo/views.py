from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Demo
from .serializers import DemoCreateSerializer, DemoSerializer
from .filters import DemoFilter
from .paginations import DemoPagination
from accounts.permissions import IsTeamLeader


class DemoViewSet(ModelViewSet):
    pagination_class = DemoPagination
    filterset_class = DemoFilter
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    serializer_classes = {
        "create": DemoCreateSerializer,
    }
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

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
