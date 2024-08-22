from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

# from yangiliklarapp.views import news_router, category_router


schema_view = get_schema_view(
    openapi.Info(
        title="News List Api",
        default_version='v1',
        description="News demo Project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="igamberdiyevabdullo3@gmail.com"),
        license=openapi.License(name="demo License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('yangiliklarapp.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(news_router.urls)),
    # path('api/v1/', include(category_router.urls)),
    # Swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name="swagger-swagger-ui"),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
