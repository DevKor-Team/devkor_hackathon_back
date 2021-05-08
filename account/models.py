from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Position(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    team = models.ManyToManyField(
        Team, on_delete=models.SET_NULL, related_name="user_set", null=True
    )
    url = models.URLField(blank=True)
    position = models.ManyToManyField(
        Position, on_delete=models.SET_NULL, related_name="user_set", null=True
    )
