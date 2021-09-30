from django.contrib import admin

from apps.portfolio import models


# @admin.register(models.ProjectTechnology)
# class ProjectTechnologyAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
#         if db_field.name == "technology":
#             kwargs["queryset"] = db_field.related_model.objects.filter(brand_type__name=models.BrandTypeNameEnum.TECHNOLOGY.value)
#         return super(ProjectTechnologyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(models.Project)
admin.site.register(models.ProjectImages)
admin.site.register(models.Brand)
admin.site.register(models.BrandType)
admin.site.register(models.MyBullet)
admin.site.register(models.BulletGroup)
admin.site.register(models.WebsiteSettings)
