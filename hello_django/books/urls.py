from django.urls import path

from .views import book_list


urlpatterns = [
    path('book-list/', book_list),
]
