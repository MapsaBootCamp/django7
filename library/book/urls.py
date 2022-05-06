from django.urls import path

from .views import BookList, BookDetail


urlpatterns = [
    path('book-list/', BookList.as_view(), name="book_list"),
    path('book-detail/<slug:id>', BookDetail.as_view(), name="book_detail"),
]
