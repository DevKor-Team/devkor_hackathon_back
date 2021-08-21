from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VoteSchedule
from .serializers import VoteSerializer


class VoteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        req_votes = request.data
        schedule = VoteSchedule.currently()

        if not schedule:
            return Response(
                {"error": "No vote schedule is currently active."}, status=400
            )

        if schedule.max_votes != len(req_votes):
            return Response({"error": "Too many or less votes."}, status=400)

        votes = [
            {
                "team": vote.get("team"),
                "demo": vote.get("demo"),
                "priority": i + 1,
                "schedule": schedule.id,
            }
            for i, vote in enumerate(req_votes)
        ]

        serializer = VoteSerializer(data=votes, many=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VotableAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_response(self, votable):
        return Response({"votable": votable})

    def get(self, request, *args, **kwargs):
        schedule = VoteSchedule.currently()

        if not schedule:
            return self.get_response(False)

        # TODO team year
        for team in request.user.teams.all():
            if (not team.voted(schedule)) and (team.leader == request.user):
                return self.get_response(True)

        return self.get_response(False)
