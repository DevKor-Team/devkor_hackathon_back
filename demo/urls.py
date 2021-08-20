from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("demo", views.DemoViewSet)
router.register("comments", views.CommentViewSet)
router.register("emoji", views.EmojiViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("image", views.DemoImageView.as_view()),
    path("tags", views.TechStackTagView.as_view()),
]
