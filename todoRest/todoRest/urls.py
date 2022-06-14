from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

def index(request):
    messages.info(request, "Khosh Amadi")
    return redirect('/admin/')


urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include("app.urls")),
    path('api-token-auth/', views.obtain_auth_token),  ## login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
