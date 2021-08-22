from django.contrib import admin
from vote.models import Scoring, Vote, VoteSchedule


admin.site.register(Vote)


class VoteInlineAdmin(admin.TabularInline):
    model = Vote


admin.site.register(Scoring)


class ScoringInlineAdmin(admin.TabularInline):
    model = Scoring


class VoteScheduleAdmin(admin.ModelAdmin):
    list_display = ["start_at", "end_at", "is_test"]
    list_filter = ["start_at", "end_at", "is_test"]

    inlines = [
        ScoringInlineAdmin,
        VoteInlineAdmin,
    ]


admin.site.register(VoteSchedule, VoteScheduleAdmin)
