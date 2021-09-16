from django.urls import include, path
from rest_framework import routers

from apps.portfolio import views

app_name = "portfolio"
router = routers.DefaultRouter()

router.register("projects", views.ProjectViewSet, basename="projects")
router.register("sections", views.PageSectionViewSet, basename="sections")

urlpatterns = [
    path("", include(router.urls)),
]
