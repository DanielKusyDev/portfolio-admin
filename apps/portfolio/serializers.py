from rest_framework import serializers

from apps.portfolio.models import Project, ProjectPageSection


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "url", "code_url", "thumbnail"]


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPageSection
        fields = ["project", "number", "header", "text_body", "image"]
