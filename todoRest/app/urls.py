from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import CategoryDetailView, CategoryView, UserViewset, PostInstaView, TodoDetail, TodoList, PostInstagramiViewSet

router = DefaultRouter()
router.register("posts", PostInstagramiViewSet, basename="postinstagrami")
router.register("accounts", UserViewset, basename="account")

urlpatterns = [
    path('todo-list/', TodoList.as_view(), name="todo_list"),
    path('todo-detail/<int:pk>', TodoDetail.as_view(), name="todo_detail"),
    path('category-list/', CategoryView.as_view(), name="category_list"),
    path('category-detail/<int:pk>', CategoryDetailView.as_view(), name="category-detail"),
    # path('posts/', PostInstaView.as_view(), name="posts"),
] + router.urls
