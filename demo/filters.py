from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Demo


class DemoFilter(filters.FilterSet):

    year = filters.NumberFilter(
        field_name="created_at",
        label="연도",
        lookup_expr="year"
    )

    tag = filters.CharFilter(
        field_name="tags",
        method="get_tag"
    )

    tech_stack = filters.CharFilter(
        field_name="tech_stacks",
        method="get_tech_stack"
    )

    @staticmethod
    def get_tag(queryset, name, value):
        return queryset.filter(
            tags__name=value
        ).distinct()

    @staticmethod
    def get_tech_stack(queryset, name, value):
        return queryset.filter(
            tech_stacks__name=value
        ).distinct()

    class Meta:
        model = Demo
        fields = {
            "created_at": [
                "exact"
            ],
            "tags": [
            ],
            "tech_stacks": [
            ],
        }
