from rest_framework import serializers

from apps.portfolio import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ["id", "name", "description", "url", "code_url", "thumbnail"]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = "__all__"


class PortfolioInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PortfolioInfo
        fields = "__all__"


class _SingleBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyBullet
        fields = ["name", "order"]


class MyBulletSerializer(serializers.ModelSerializer):
    bullets = _SingleBulletSerializer(many=True, read_only=True)

    class Meta:
        model = models.BulletGroup
        fields = "__all__"
