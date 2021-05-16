from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import mixins

from accounts.models import User
from accounts.serializers import UserSerializer, ProfileSerializer


class ProfileViewSet(GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]  # TODO IsMyProfile


class MeView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
