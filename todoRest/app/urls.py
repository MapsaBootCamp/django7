from django.urls import path
from django.views.decorators.cache import cache_page

from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import CategoryDetailView, CategoryView, FollowerCRUD, GherUmadan, Kabareh, SendSms, UserViewset, PostInstaView, TodoDetail, TodoList, PostInstagramiViewSet

router = DefaultRouter()
router.register("posts", PostInstagramiViewSet, basename="postinstagrami")
router.register("accounts", UserViewset, basename="account")
router.register("follow-action", FollowerCRUD, basename="follow_action")
urlpatterns = [
    path('todo-list/', TodoList.as_view(), name="todo_list"),
    path('sms/', SendSms.as_view(), name="sms"),
    path('todo-detail/<int:pk>', TodoDetail.as_view(), name="todo_detail"),
    path('category-list/', CategoryView.as_view(), name="category_list"),
    path('category-detail/<int:pk>', CategoryDetailView.as_view(), name="category-detail"),
    # path('posts/', PostInstaView.as_view(), name="posts"),
    path('gher/', Kabareh.as_view(), name="gher"),
] + router.urls
