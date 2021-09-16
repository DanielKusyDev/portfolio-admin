from django.db import models

from apps.portfolio.models_utils import get_encoded_file_name


class Project(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    code_url = models.URLField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to=get_encoded_file_name, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ProjectPageSection(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="sections")
    number = models.PositiveIntegerField()
    header = models.CharField(max_length=511, null=True, blank=True)
    text_body = models.TextField()
    image = models.ImageField(upload_to=get_encoded_file_name, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.project.name}, s. {self.number}, {' '.join(self.text_body.split()[:5])}..."

    class Meta:
        unique_together = ["project", "number"]
