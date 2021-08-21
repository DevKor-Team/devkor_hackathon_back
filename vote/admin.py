from django.contrib import admin
from vote.models import Vote, VoteSchedule


admin.site.register(Vote)
admin.site.register(VoteSchedule)
