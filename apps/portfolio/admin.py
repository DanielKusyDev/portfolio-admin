from django.contrib import admin

from apps.portfolio import models

admin.site.register(models.Project)
admin.site.register(models.ProjectImages)
admin.site.register(models.SocialMedia)
admin.site.register(models.MyBullet)
admin.site.register(models.BulletGroup)
admin.site.register(models.PortfolioInfo)
