from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        team = validated_data["team"]
        demo = validated_data["demo"]
        schedule = validated_data["schedule"]
        user = self.context["request"].user

        if team.voted(schedule):
            raise serializers.ValidationError("You have already voted")

        if demo.team not in user.teams.all():
            if team.leader == user:
                vote, _ = Vote.objects.get_or_create(
                    team=team,
                    demo=demo,
                    schedule=schedule,
                )
                vote.priority = validated_data["priority"]
                vote.save()
                return vote
            else:
                raise serializers.ValidationError("Only team leader can vote")
        else:
            raise serializers.ValidationError("You can't vote for your team")

    class Meta:
        model = Vote
        fields = "__all__"
