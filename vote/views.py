from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import Vote
from .serializers import VoteSerializer


class VoteViewSet(GenericViewSet, mixins.CreateModelMixin):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
