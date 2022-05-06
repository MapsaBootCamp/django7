from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book/', include("book.urls")),
    path('api/rent/', include("rent.urls")),
]
