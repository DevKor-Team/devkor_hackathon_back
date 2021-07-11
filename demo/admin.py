from django.contrib import admin
from .models import Demo, Tag, TechStackTag


admin.site.register(Demo)
admin.site.register(Tag)
admin.site.register(TechStackTag)
