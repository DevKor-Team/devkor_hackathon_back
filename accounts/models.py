from datetime import timedelta
from hashlib import sha256

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

from accounts.services import no_padding_b64encode, no_padding_b64decode


User = get_user_model()


# TODO team year
class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name="teams")
    leader = models.ForeignKey(
        User, related_name="leader_teams", on_delete=models.SET_NULL, null=True
    )

    def sign_token(self, timestamp: bytes):
        return sha256(
            self.name.encode() + timestamp + settings.SECRET_KEY.encode()
        ).digest()

    def create_token(self):
        expire = (timezone.now() + timedelta(hours=6)).timestamp()
        expire_bytes = int(expire).to_bytes(5, byteorder="little")
        sign = self.sign_token(expire_bytes)
        return no_padding_b64encode(expire_bytes + sign).decode()

    def verify_token(self, token):
        try:
            token_decoded = no_padding_b64decode(token.encode())
            expire_bytes = token_decoded[:5]
            sign = token_decoded[5:]
            expire = int.from_bytes(expire_bytes, byteorder="little")
        except:
            return False

        if expire < timezone.now().timestamp():
            return False

        if sign != self.sign_token(expire_bytes):
            return False

        return True

    def voted(self, schedule):
        return self.votes.filter(schedule=schedule).count() >= schedule.max_votes

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    url = models.URLField(blank=True)
    position = models.CharField(max_length=128, default="developer", blank=True)
    bio = models.TextField(
        default="The best developer in the infinite universe.", blank=True
    )
    profile_img = models.ImageField(upload_to="profile_img", blank=True)

    def __str__(self):
        return f"<{self.user.username}> {self.user.first_name} {self.user.last_name}"
