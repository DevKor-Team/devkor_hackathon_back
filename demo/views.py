from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from devathon.mixins import ActionPermission, ActionSerializer

from .models import Demo, DemoImage, Comment, Emoji
from .serializers import (
    DemoCreateSerializer,
    DemoImageSerializer,
    DemoSerializer,
    CommentSerializer,
    EmojiSerializer,
)
from .filters import DemoFilter
from .paginations import DemoPagination
from .permissions import (
    IsEmojiWriter,
    IsImageOfMyDemo,
    IsDemoTeamLeader,
    IsCommentWriter,
)


class DemoViewSet(ModelViewSet, ActionPermission, ActionSerializer):
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


class DemoImageView(CreateAPIView):
    queryset = DemoImage.objects.all()
    serializer_class = DemoImageSerializer
    permission_classes = [IsImageOfMyDemo]
    lookup_field = "id"


class CommentViewSet(ModelViewSet, ActionPermission):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = {
        "list": [],
        "create": [],
        "retreive": [],
        "update": [IsCommentWriter],
        "destroy": [IsCommentWriter],
    }


class EmojiViewSet(ModelViewSet, ActionPermission):
    queryset = Emoji.objects.all()
    serializer_class = EmojiSerializer
    permission_classes = {
        "list": [],
        "create": [],
        "retreive": [],
        "update": [IsEmojiWriter],
        "destroy": [IsEmojiWriter],
    }
