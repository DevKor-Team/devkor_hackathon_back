from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("demo", views.DemoViewSet)

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
