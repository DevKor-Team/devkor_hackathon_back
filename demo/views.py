from django.db.models import Q
from rest_framework import decorators
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.mixins import DestroyModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser

from devathon.viewsets import ActionModelViewSet, ActionViewSet

from .models import Demo, DemoImage, Comment, Emoji, TechStackTag
from .serializers import (
    CommentCreateSerializer,
    DemoCreateSerializer,
    DemoImageSerializer,
    DemoSerializer,
    CommentSerializer,
    EmojiSerializer,
    TechStackTagSerializer,
)
from .filters import DemoFilter, EmojiFilter
from .permissions import (
    IsEmojiWriter,
    IsImageOfMyDemo,
    IsDemoTeamLeader,
    IsCommentWriter,
)


class DemoViewSet(ActionModelViewSet):
    filterset_class = DemoFilter
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    serializer_classes = {
        "create": DemoCreateSerializer,
    }
    action_permission_classes = {
        "list": [],
        "retreive": [],
        "partial_update": [IsDemoTeamLeader],
        "update": [IsDemoTeamLeader],
        "destroy": [IsDemoTeamLeader | IsAdminUser],
        "emoji": [],
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Demo.objects.filter(
                Q(show=True) | Q(team__users=self.request.user)
            ).distinct()
        else:
            return Demo.objects.filter(show=True)

    @decorators.action(detail=True, methods=["POST"])
    def emoji(self, request, *args, **kwargs):
        typ = request.data.get("typ", None)
        demo = self.get_object()
        demo.leave_emoji(request.user, typ)
        return self.retrieve(request, *args, **kwargs)


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
        "retreive": [],
        "partial_update": [IsCommentWriter],
        "update": [IsCommentWriter],
        "destroy": [IsCommentWriter],
        "like": [],
        "dislike": [],
    }

    @decorators.action(detail=True, methods=["POST"])
    def like(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.like(request.user)
        return self.retrieve(request, *args, **kwargs)

    @decorators.action(detail=True, methods=["POST"])
    def dislike(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.dislike(request.user)
        return self.retrieve(request, *args, **kwargs)


class EmojiViewSet(ActionViewSet, ListModelMixin, DestroyModelMixin):
    queryset = Emoji.objects.all()
    filterset_class = EmojiFilter
    serializer_class = EmojiSerializer
    action_permission_classes = {
        "list": [],
        "destroy": [IsEmojiWriter],
    }

    def get_queryset(self):
        return self.queryset.filter(writer=self.request.user)


class TechStackTagView(ListAPIView):
    queryset = TechStackTag.objects.all()
    serializer_class = TechStackTagSerializer
    permission_classes = []
