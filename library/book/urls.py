from django.urls import path

from .views import BookList, BookDetail, book_list


urlpatterns = [
    path('book-list/', book_list, name="book_list_template"),
    path('api/book-list/', BookList.as_view(), name="book_list"),
    path('api/book-detail/<slug:id>', BookDetail.as_view(), name="book_detail"),
]
