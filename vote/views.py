from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VoteSchedule
from .serializers import VoteSerializer


class VoteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        team_id = request.data.get("team")
        demo_ids = request.data.get("demo", [])
        schedule = VoteSchedule.currently()

        if schedule.is_test and not request.user.is_staff:
            return Response({"detail": "Test voting is not allowed."}, status=403)

        if not schedule:
            return Response(
                {"error": "No vote schedule is currently active."}, status=400
            )

        if schedule.max_votes != len(demo_ids):
            return Response({"error": "Too many or less votes."}, status=400)

        votes = [
            {
                "team": team_id,
                "demo": demo_id,
                "priority": i + 1,
                "schedule": schedule.id,
            }
            for i, demo_id in enumerate(demo_ids)
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

        if schedule.is_test and not request.user.is_staff:
            return self.get_response(False)

        # TODO team year
        for team in request.user.teams.all():
            if (not team.voted(schedule)) and (team.leader == request.user):
                return self.get_response(True)

        return self.get_response(False)


class VoteResultAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        schedule = VoteSchedule.past()

        if schedule.count() < 1:
            return Response({"error": "No past vote schedule."}, status=404)

        if not request.user.is_staff:
            return Response({"error": "No permission."}, status=403)

        return Response(schedule.last().get_result())
