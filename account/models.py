from datetime import timedelta
from hashlib import sha256

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from devathon.settings.base import SECRET_KEY
from account.services import no_padding_b64encode, no_padding_b64decode


User = get_user_model()


class Position(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    token = models.CharField(max_length=128)

    def sign_token(self, timestamp: bytes):
        return sha256(self.name.encode() + timestamp + SECRET_KEY.encode()).digest()

    def create_token(self):
        expire = (timezone.now() + timedelta(hours=1)).timestamp()
        expire_bytes = int(expire).to_bytes(5, byteorder="little")
        sign = self.sign_token(expire_bytes)
        self.token = no_padding_b64encode(expire_bytes + sign)

    def verify_token(self, token):
        try:
            token_decoded = no_padding_b64decode(token)
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    team = models.ManyToManyField(Team, related_name="user_set", null=True)
    url = models.URLField(blank=True)
    position = models.ManyToManyField(Position, related_name="user_set", null=True)
