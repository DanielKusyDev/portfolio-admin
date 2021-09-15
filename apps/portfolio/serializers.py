from rest_framework import serializers

from apps.portfolio.models import Project, ProjectPageSection, SectionMedia


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "description", "url"]


class PageSectionSerializer(serializers.ModelSerializer):
    media = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="portfolio:section_media-detail")

    class Meta:
        model = ProjectPageSection
        fields = ["project", "number", "header", "text_body", "media"]


class SectionMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionMedia
        fields = ["image"]
