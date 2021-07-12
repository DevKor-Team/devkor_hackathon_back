from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Demo


class DemoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tech_stacks = TagListSerializerField()
    tags = TagListSerializerField()

    class Meta:
        model = Demo
        fields = ["id", "team", "title", "thumbnail", "desc", "created_at", "tech_stacks", "tags"]
