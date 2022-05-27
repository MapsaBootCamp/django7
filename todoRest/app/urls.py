from django.urls import path

from .views import CategoryDetailView, CategoryView, TodoDetail, TodoList


urlpatterns = [
    path('todo-list/', TodoList.as_view(), name="todo_list"),
    path('todo-detail/<int:pk>', TodoDetail.as_view(), name="todo_detail"),
    path('category-list/', CategoryView.as_view(), name="category_list"),
    path('category-detail/<int:pk>', CategoryDetailView.as_view(), name="category-detail"),
]
