from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version="v1",
        description="API for Daniel's portfolio page",
        contact=openapi.Contact(email="daniel.kusy97@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.portfolio.urls", namespace="portfolio")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
