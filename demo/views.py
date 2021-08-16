from rest_framework import decorators
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from devathon.viewsets import ActionModelViewSet

from .models import Demo, DemoImage, Comment, Emoji
from .serializers import (
    CommentCreateSerializer,
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


class DemoViewSet(ActionModelViewSet):
    pagination_class = DemoPagination
    filterset_class = DemoFilter
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    serializer_classes = {
        "create": DemoCreateSerializer,
    }
    action_permission_classes = {
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


class CommentViewSet(ActionModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_classes = {
        "create": CommentCreateSerializer,
    }
    action_permission_classes = {
        "list": [],
        "create": [],
        "retreive": [],
        "update": [IsCommentWriter],
        "destroy": [IsCommentWriter],
    }

    @decorators.action(detail=True, methods=["POST"])
    def like(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.like(request.user)
        return self.retrieve(request, *args, **kwargs)


class EmojiViewSet(ActionModelViewSet):
    queryset = Emoji.objects.all()
    serializer_class = EmojiSerializer
    action_permission_classes = {
        "list": [],
        "create": [],
        "retreive": [],
        "update": [IsEmojiWriter],
        "destroy": [IsEmojiWriter],
    }
