from django.urls import include, path
from rest_framework import routers

from apps.portfolio import views

app_name = "portfolio"
router = routers.DefaultRouter()

router.register("projects", views.ProjectViewSet, basename="projects")
router.register("sections", views.PageSectionViewSet, basename="sections")
router.register("section_media", views.SectionMediaViewSet, basename="section_media")

urlpatterns = [
    path("", include(router.urls)),
]
