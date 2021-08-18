from rest_framework.pagination import PageNumberPagination
from .models import Demo


class DemoPagination(PageNumberPagination):
    page_size = 6
