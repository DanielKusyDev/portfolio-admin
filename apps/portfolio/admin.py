from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from apps.portfolio.models import Project, ProjectPageSection, SectionMedia

admin.site.register(Project)
admin.site.register(SectionMedia)
admin.site.register(ProjectPageSection)
