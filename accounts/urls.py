from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register("profile", views.ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("me/", views.MeView.as_view()),
]
