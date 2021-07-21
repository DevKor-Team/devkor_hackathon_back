from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Demo, DemoImage
from accounts.serializers import TeamSerializer
from accounts.models import Team


class DemoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tech_stacks = TagListSerializerField()
    tags = TagListSerializerField()
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Demo
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class DemoCreateSerializer(DemoSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())


class DemoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoImage
        fields = "__all__"
