from rest_framework import serializers

from apps.portfolio import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ["id", "name", "short_description", "description", "url", "code_url", "thumbnail"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class WebsiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WebsiteSettings
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
