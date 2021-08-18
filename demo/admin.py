from django.contrib import admin
from .models import Demo, Tag, TechStackTag, Comment


admin.site.register(Demo)
admin.site.register(Tag)
admin.site.register(TechStackTag)
admin.site.register(Comment)
