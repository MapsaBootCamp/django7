from django.urls import path

from .views import BookRentView


urlpatterns = [
    path('', BookRentView.as_view(), name="book_rent"),
]
