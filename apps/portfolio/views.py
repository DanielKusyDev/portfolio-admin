import django_filters
from rest_framework.viewsets import ModelViewSet

from apps.portfolio.serializers import (
    ProjectSerializer,
    PageSectionSerializer,
    SectionMediaSerializer,
)
from apps.portfolio.models import Project, ProjectPageSection, SectionMedia


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ["get"]


class PageSectionViewSet(ModelViewSet):
    queryset = ProjectPageSection.objects.all()
    serializer_class = PageSectionSerializer
    http_method_names = ["get"]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["project"]


class SectionMediaViewSet(ModelViewSet):
    queryset = SectionMedia.objects.all()
    serializer_class = SectionMediaSerializer
    http_method_names = ["get"]
