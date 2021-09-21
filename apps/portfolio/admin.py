from django.contrib import admin

from apps.portfolio.models import Project, ProjectPageSection, SocialMedia

admin.site.register(Project)
admin.site.register(ProjectPageSection)
admin.site.register(SocialMedia)
