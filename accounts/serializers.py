from rest_framework import serializers
from accounts.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]

    def create(self, validated_data):
        user = self.context["request"].user
        profile = Profile(**validated_data, user=user)
        profile.save()
        return profile


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

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
