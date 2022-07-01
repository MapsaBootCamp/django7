from django.contrib import admin
from django.http import HttpResponse
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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
