import django_filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from apps.portfolio import models, serializers
from apps.portfolio.models import BrandTypeNameEnum


class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    http_method_names = ["get"]


class SocialMediaApiView(ListAPIView):
    queryset = models.Brand.objects.filter(brand_type__name=BrandTypeNameEnum.SOCIAL_MEDIA.value)
    serializer_class = serializers.BrandSerializer


class TechnologiesApiView(ListAPIView):
    queryset = models.Brand.objects.filter(brand_type__name=BrandTypeNameEnum.TECHNOLOGY.value)
    serializer_class = serializers.BrandSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["projects"]


class MyBulletApiView(ListAPIView):
    queryset = models.BulletGroup.objects.all()
    serializer_class = serializers.MyBulletSerializer


class WebsiteSettingsApiView(RetrieveAPIView):
    serializer_class = serializers.WebsiteSettingsSerializer

    def get_object(self) -> models.WebsiteSettings:
        return models.WebsiteSettings.objects.first()
