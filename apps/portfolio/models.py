from django.db import models

from apps.portfolio.models_utils import get_encoded_file_name


class Project(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    url = models.URLField()

    def __str__(self) -> str:
        return self.name


class ProjectPageSection(models.Model):
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="sections"
    )
    number = models.PositiveIntegerField()
    header = models.CharField(max_length=511)
    text_body = models.TextField()

    def __str__(self) -> str:
        return f"{self.project.name}, s. {self.number}, {' '.join(self.text_body.split()[:5])}..."


class SectionMedia(models.Model):
    image = models.ImageField(upload_to=get_encoded_file_name)
    section = models.ForeignKey(
        to=ProjectPageSection, on_delete=models.CASCADE, related_name="media"
    )

    def __str__(self) -> str:
        return f"{self.section.project}, {self.section.number}, {self.image.name}"
