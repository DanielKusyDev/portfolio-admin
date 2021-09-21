import django_filters
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.portfolio.models import Project, ProjectPageSection, SocialMedia
from apps.portfolio.serializers import PageSectionSerializer, ProjectSerializer, SocialMediaSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ["get"]


class PageSectionViewSet(ModelViewSet):
    queryset = ProjectPageSection.objects.order_by("number")
    serializer_class = PageSectionSerializer
    http_method_names = ["get"]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["project"]


class SocialMediaApiView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
