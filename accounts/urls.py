from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register("profile/", views.ProfileViewSet)

urlpatterns = [
    path("me/", views.MeView.as_view()),
]
