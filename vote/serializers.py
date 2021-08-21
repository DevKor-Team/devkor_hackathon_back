from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        team = validated_data["team"]
        demo = validated_data["demo"]
        user = self.context["request"].user
        if demo.team not in user.teams.all():
            if team.leader == user:
                return Vote.objects.create(**validated_data)
            else:
                raise serializers.ValidationError("Only team leader can vote")
        else:
            raise serializers.ValidationError("You can't vote for your team")

    class Meta:
        model = Vote
        fields = "__all__"
