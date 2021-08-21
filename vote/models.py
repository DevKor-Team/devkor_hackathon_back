from django.db import models
from django.utils import timezone

from accounts.models import Team
from demo.models import Demo


class VoteSchedule(models.Model):
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(default=timezone.now)

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


class Vote(models.Model):
    team = models.ForeignKey(Team, related_name="votes", on_delete=models.CASCADE)
    demo = models.ForeignKey(Demo, related_name="votes", on_delete=models.CASCADE)
    schedule = models.ForeignKey(
        VoteSchedule, related_name="votes", on_delete=models.CASCADE
    )
    priority = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.user, self.demo)
