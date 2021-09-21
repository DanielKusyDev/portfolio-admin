from rest_framework import serializers

from apps.portfolio.models import Project, ProjectPageSection, SocialMedia


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "url", "code_url", "thumbnail"]


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPageSection
        fields = ["project", "number", "header", "text_body", "image"]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"
