from django.db import models
from accounts.models import Team, User
from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase


class Tag(TagBase):
    # NOTE: django-taggit does not allow unicode by default.
    slug = models.SlugField(
        unique=True,
        max_length=128,
        allow_unicode=True,
    )


class TechStackTag(TagBase):
    # NOTE: django-taggit does not allow unicode by default.
    slug = models.SlugField(
        unique=True,
        max_length=128,
        allow_unicode=True,
    )


class TaggedDemo(TaggedItemBase):
    content_object = models.ForeignKey(
        "Demo",
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        "Tag",
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE,
    )


class TechStackTaggedDemo(TaggedItemBase):
    content_object = models.ForeignKey(
        "Demo",
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        "TechStackTag",
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE,
    )


class Demo(models.Model):
    team = models.OneToOneField(
        Team, on_delete=models.CASCADE, related_name="demo", unique=True
    )
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="images/")
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tech_stacks = TaggableManager(
        blank=True,
        through=TechStackTaggedDemo,
    )
    tags = TaggableManager(
        blank=True,
        through=TaggedDemo,
    )

    class Meta:
        ordering = ["-created_at"]

    @property
    def like_count(self):
        return self.emojis.filter(typ="LK").count()

    @property
    def wow_count(self):
        return self.emojis.filter(typ="WW").count()

    @property
    def fire_count(self):
        return self.emojis.filter(typ="FR").count()

    @property
    def fun_count(self):
        return self.emojis.filter(typ="FN").count()

    @property
    def sad_count(self):
        return self.emojis.filter(typ="SD").count()

    def leave_emoji(self, user, typ):
        emoji, created = Emoji.objects.get_or_create(
            writer=user,
            demo=self,
            typ=typ,
        )
        if not created:
            emoji.delete()
        return emoji

    def __str__(self):
        return f"<{self.team.name}> {self.title}"


class DemoImage(models.Model):
    demo = models.ForeignKey(Demo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")


class Comment(models.Model):
    writer = models.ForeignKey(User, related_name="comments", on_delete=models.PROTECT)
    demo = models.ForeignKey(Demo, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likers = models.ManyToManyField(User, related_name="liked_comments", blank=True)
    dislikers = models.ManyToManyField(
        User, related_name="disliked_comments", blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    @property
    def likes(self):
        return self.likers.count()

    @property
    def dislikes(self):
        return self.dislikers.count()

    def like(self, user):
        if user in self.likers.all():
            self.likers.remove(user)
        else:
            self.dislikers.remove(user)
            self.likers.add(user)
        self.save()

    def dislike(self, user):
        if user in self.dislikers.all():
            self.dislikers.remove(user)
        else:
            self.likers.remove(user)
            self.dislikers.add(user)
        self.save()

    def __str__(self):
        return (
            f"<{self.demo.title}:{self.writer.username}> "
            + "{:<15}".format(self.content[:15])
            + f" ({self.created_at})"
        )


class EmojiTypes(models.TextChoices):
    LIKE = "LK", "좋아요"
    WOW = "WW", "놀라워요"
    FIRE = "FR", "불"
    FUN = "FN", "웃겨요"
    SAD = "SD", "슬퍼요"


class Emoji(models.Model):
    writer = models.ForeignKey(User, related_name="emojis", on_delete=models.PROTECT)
    demo = models.ForeignKey(Demo, related_name="emojis", on_delete=models.CASCADE)
    typ = models.CharField(
        max_length=2, choices=EmojiTypes.choices, default=EmojiTypes.LIKE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"<{self.demo.title}:{self.writer.username}> {self.typ} ({self.created_at})"
        )
