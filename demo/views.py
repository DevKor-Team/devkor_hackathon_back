from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Demo, DemoImage
from .serializers import DemoCreateSerializer, DemoImageSerializer, DemoSerializer
from .filters import DemoFilter
from .paginations import DemoPagination
from .permissions import IsImageOfMyDemo, IsDemoTeamLeader


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
        "create": [],
        "retreive": [],
        "update": [IsDemoTeamLeader],
        "destroy": [IsDemoTeamLeader | IsAdminUser],
    }

    def get_permissions(self):
        return [
            permission() for permission in self.permission_classes.get(self.action, [])
        ]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class DemoImageView(CreateAPIView):
    queryset = DemoImage.objects.all()
    serializer_class = DemoImageSerializer
    permission_classes = [IsImageOfMyDemo]
    lookup_field = "id"
