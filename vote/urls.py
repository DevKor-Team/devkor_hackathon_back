from django.urls import path
from . import views

urlpatterns = [
    path("vote", views.VoteAPIView.as_view()),
    path("votable", views.VotableAPIView.as_view()),
    path("result", views.VoteResultAPIView.as_view()),
]
