from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
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
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/v1/', include(news_router.urls)),
    # path('api/v1/', include(category_router.urls)),
    # Swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name="swagger-swagger-ui"),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
