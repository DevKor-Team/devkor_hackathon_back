from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/oauth/", include("allauth.urls")),
    path("api/account/", include("accounts.urls")),
    path("api/demo/", include("demo.urls")),
    path("api/vote/", include("vote.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
