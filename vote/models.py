from django.db import models
from django.utils import timezone

from accounts.models import Team
from demo.models import Demo


class VoteSchedule(models.Model):
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(default=timezone.now)
    max_votes = models.SmallIntegerField(default=3)
    is_test = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.start_at, self.end_at)

    @staticmethod
    def currently():
        schedule = VoteSchedule.objects.filter(
            start_at__lte=timezone.now(),
            end_at__gte=timezone.now(),
        )
        if schedule.count() == 1:
            return schedule[0]
        else:
            return None

    @staticmethod
    def past():
        return VoteSchedule.objects.filter(
            end_at__lte=timezone.now(),
        )

    def get_result(self):
        votes = Vote.objects.filter(schedule=self)
        scorings = Scoring.objects.filter(schedule=self)
        result = {}

        scores = {}

        for scoring in scorings:
            scores[scoring.priority] = scoring.score

        for vote in votes:
            score = scores[vote.priority]
            team = vote.demo.team.name
            if team not in result:
                result[team] = 0
            result[team] += score

        return result


class Scoring(models.Model):
    schedule = models.ForeignKey(
        VoteSchedule, related_name="scoring", on_delete=models.CASCADE
    )
    priority = models.SmallIntegerField(default=0)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.schedule, self.priority)


class Vote(models.Model):
    team = models.ForeignKey(Team, related_name="votes", on_delete=models.CASCADE)
    demo = models.ForeignKey(Demo, related_name="votes", on_delete=models.CASCADE)
    schedule = models.ForeignKey(
        VoteSchedule, related_name="votes", on_delete=models.CASCADE
    )
    priority = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.team, self.demo)
