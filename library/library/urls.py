from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from book.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('book/', include("book.urls")),
    path('api/rent/', include("rent.urls")),
    path('user/', include("user.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)