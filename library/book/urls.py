from django.urls import path

from .views import BookList, BookDetail, book_list, book_detail, add_comment, BookListV1, BookDetailV2


urlpatterns = [
    path("add-comment/<int:book_id>", add_comment, name="book_add_comment"),
    # path('book-list/', BookListV1.as_view(), name="book_list_template"),
    path('book-list/', book_list, name="book_list_template"),
    path('book-detail/<int:id>', BookDetailV2.as_view(), name="book_detail_template"),
    path('api/book-list/', BookList.as_view(), name="book_list"),
    path('api/book-detail/<int:id>', BookDetail.as_view(), name="book_detail"),
]
