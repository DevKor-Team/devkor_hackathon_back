from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/oauth/", include("allauth.urls")),
    path("api/account/", include("accounts.urls")),
]
