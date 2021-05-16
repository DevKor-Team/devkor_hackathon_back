from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path("me", views.MeView.as_view()),
]
