from django.urls import path

from .views import todo_list, todo_detail

urlpatterns = [
    path("", todo_list),
    path("todo-detail/<str:username>", todo_detail),
]
