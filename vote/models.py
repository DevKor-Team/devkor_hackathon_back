from django.db import models

from accounts.models import Team
from demo.models import Demo


class Vote(models.Model):
    team = models.ForeignKey(Team, related_name="votes", on_delete=models.CASCADE)
    demo = models.ForeignKey(Demo, related_name="votes", on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.user, self.demo)
