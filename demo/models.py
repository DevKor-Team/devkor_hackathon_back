from django.db import models
from accounts.models import Team
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase, TaggedItemBase
)


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
        'Demo',
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        'Tag',
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE,
    )


class TechStackTaggedDemo(TaggedItemBase):
    content_object = models.ForeignKey(
        'Demo',
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        'TechStackTag',
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE,
    )


class Demo(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, unique=True)
    title = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to='images/')
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tech_stacks = TaggableManager(
        blank=True,
        through=TaggedDemo,
    )
    tags = TaggableManager(
        blank=True,
        through=TechStackTaggedDemo,
    )
