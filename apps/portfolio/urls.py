from django.urls import include, path
from rest_framework import routers

from apps.portfolio import views

app_name = "portfolio"
router = routers.DefaultRouter()

router.register("projects", views.ProjectViewSet, basename="projects")
router.register("sections", views.PageSectionViewSet, basename="sections")

urlpatterns = [
    path("", include(router.urls)),
    path("info/social_media/", views.SocialMediaApiView.as_view()),
    path("info/my_bullets/", views.MyBulletApiView.as_view()),
    path("info/website/", views.WebsiteSettingsApiView.as_view()),
]
