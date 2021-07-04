from django.db import models
from django.utils import timezone
from accounts.models import Team
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase, TaggedItemBase
)


class Demo(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, unique=True)
    title = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to='images/')
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tech_stack = TaggableManager(
        verbose_name=_('tech_stack'),
        blank=True,
        through=TaggedDemo,
    )
    tags = TaggableManager(
        verbose_name=_('tags'),
        blank=True,
        through=TaggedDemo,
    )


class Tag(TagBase):
    # NOTE: django-taggit does not allow unicode by default.
    slug = models.SlugField(
        verbose_name=_('slug'),
        unique=True,
        max_length=128,
        allow_unicode=True,
    )

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def slugify(self, tag, i=None):
        return default_slugify(tag, allow_unicode=True)


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

    class Meta:
        verbose_name = _("tagged demo")
        verbose_name_plural = _("tagged demos")
