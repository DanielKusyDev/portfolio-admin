from django.urls import include, path
from rest_framework import routers

from apps.portfolio import views

app_name = "portfolio"
router = routers.DefaultRouter()

router.register("projects", views.ProjectViewSet, basename="projects")

urlpatterns = [
    path("projects/technologies/", views.TechnologiesApiView.as_view()),
    path("", include(router.urls)),
    path("info/social_media/", views.SocialMediaApiView.as_view()),
    path("info/my_bullets/", views.MyBulletApiView.as_view()),
    path("info/settings/", views.WebsiteSettingsApiView.as_view()),
]
