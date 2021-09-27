from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from apps.portfolio import models, serializers


class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    http_method_names = ["get"]


class SocialMediaApiView(ListAPIView):
    queryset = models.SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer


class MyBulletApiView(ListAPIView):
    queryset = models.BulletGroup.objects.all()
    serializer_class = serializers.MyBulletSerializer


class PortfolioInfoApiView(RetrieveAPIView):
    serializer_class = serializers.PortfolioInfoSerializer

    def get_object(self) -> models.PortfolioInfo:
        return models.PortfolioInfo.objects.first()
