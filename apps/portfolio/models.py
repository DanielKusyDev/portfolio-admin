from django.core import validators
from django.db import models
from marshmallow import ValidationError

from apps.portfolio.models_utils import get_encoded_file_name
from django.utils.translation import gettext_lazy as _


class BrandTypeNameEnum(models.TextChoices):
    SOCIAL_MEDIA = "SOCIAL", _("Social Media")
    TECHNOLOGY = "TECH", _("Technology")


class Project(models.Model):
    name = models.CharField(max_length=127)
    short_description = models.TextField()
    description = models.TextField()
    code_url = models.URLField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to=get_encoded_file_name, null=True, blank=True)
    technologies = models.ManyToManyField(
        to="Brand",
        related_name="projects",
        limit_choices_to=dict(brand_type__name=BrandTypeNameEnum.TECHNOLOGY.value),
    )

    def __str__(self) -> str:
        return self.name


class ProjectImages(models.Model):
    image = models.ImageField()
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="images")

    def __str__(self) -> str:
        return f"{self.project.name}, {self.image.name}"


class BrandType(models.Model):
    name = models.CharField(max_length=16, choices=BrandTypeNameEnum.choices)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=125, primary_key=True)
    url = models.URLField()
    icon = models.ImageField(upload_to=get_encoded_file_name)
    brand_type = models.ForeignKey(to="BrandType", on_delete=models.CASCADE, related_name="brands")

    def __str__(self) -> str:
        return self.name


class ProjectTechnology(models.Model):
    technology = models.ForeignKey(to="Brand", on_delete=models.CASCADE)
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Project technologies"
        verbose_name = "Project technology"


class MyBullet(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(to="BulletGroup", related_name="bullets", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["order", "id"]


class BulletGroup(models.Model):
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    column = models.PositiveIntegerField(choices=((0, "LEFT"), (1, "RIGHT")))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["order", "id"]


class WebsiteSettings(models.Model):
    main_title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=256, null=True, blank=True)
    summary = models.CharField(max_length=512, null=True, blank=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    theme_color = models.CharField(max_length=6, validators=[validators.MaxLengthValidator(6)], default="25639e")
    avatar = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "website settings"
        verbose_name = "website settings"

    def save(self, *args, **kwargs):
        if not self.pk and WebsiteSettings.objects.exists():
            raise ValidationError("There can be only one instance of WebsiteSettings")
        return super(WebsiteSettings, self).save(*args, **kwargs)
