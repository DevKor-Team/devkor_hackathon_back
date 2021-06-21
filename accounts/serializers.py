from rest_framework import serializers
from accounts.models import User, Profile, Team


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]

    def create(self, validated_data):
        user = self.context["request"].user
        profile = Profile(**validated_data, user=user)
        profile.save()
        return profile


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "profile",
            "username",
            "first_name",
            "last_name",
            "email",
            "last_login",
            "date_joined",
        ]


class UserSerializer(UserListSerializer):
    profile = ProfileSerializer()


class TeamSerializer(serializers.ModelSerializer):
    users = UserListSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "users"]

    def create(self, validated_data):
        team = Team(**validated_data)
        team.save()
        team.users.add(self.context["request"].user)
        team.save()
        return team
