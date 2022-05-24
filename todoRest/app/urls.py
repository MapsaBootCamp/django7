from django.urls import path

from .views import TodoDetail, TodoList


urlpatterns = [
    path('todo-list/', TodoList.as_view(), name="todo_list"),
    path('todo-detail/<int:pk>', TodoDetail.as_view(), name="todo_detail"),
]
