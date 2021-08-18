from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Comment, Demo, DemoImage, Emoji
from accounts.serializers import TeamSerializer, UserSerializer
from accounts.models import Team


class CommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            "id",
            "writer",
            "demo",
            "content",
            "created_at",
            "updated_at",
            "likes",
            "dislikes",
        ]
        read_only_fields = ["id", "writer", "demo" "created_at", "updated_at"]


class CommentCreateSerializer(serializers.ModelSerializer):
    writer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ["id", "writer", "demo", "content", "created_at"]
        read_only_fields = ["id", "created_at"]


class EmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = "__all__"
        read_only_fields = ["id", "created_at"]


class DemoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tech_stacks = TagListSerializerField()
    tags = TagListSerializerField()
    team = TeamSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Demo
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class DemoCreateSerializer(DemoSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    def create(self, validated_data):
        if validated_data["team"].leader == self.context["request"].user:
            return Demo.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("Only team leader can register")

    class Meta:
        model = Demo
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class DemoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoImage
        fields = "__all__"
