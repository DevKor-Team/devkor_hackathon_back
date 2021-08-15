from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("demo", views.DemoViewSet)
router.register("comments", views.CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("image", views.DemoImageView.as_view()),
]
