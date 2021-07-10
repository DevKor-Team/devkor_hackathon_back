from rest_framework import serializers
from .models import Demo
from accounts.serializers import TeamSerializer


class DemoSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Demo
        fields = ["id", "team", "title", "thumbnail", "desc", "created_at", "updated_at"]
