from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tasks", viewset=views.TaskViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
