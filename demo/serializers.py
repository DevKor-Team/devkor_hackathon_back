from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Demo
from accounts.serializers import TeamSerializer
from accounts.models import Team


class DemoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tech_stacks = TagListSerializerField()
    tags = TagListSerializerField()
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Demo
        fields = [
            "id",
            "team",
            "title",
            "thumbnail",
            "desc",
            "created_at",
            "tech_stacks",
            "tags",
        ]


class DemoCreateSerializer(DemoSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
