import random

from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.decorators import action

from .tasks import async_send_mail, my_multiply
from app.serializers import CategoryDetailSerializer, CategoryListSerializer, PostInstagramiListSerializer, PostInstagramiDetailSerializer, TodoDetailSerializer, TodoListSerializer, UserSerializer
from app.models import Category, PostInstagrami, Todo


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class CategoryView(APIView):
    
    permission_classes = [permissions.IsAuthenticated|ReadOnly]
    
    # @method_decorator(cache_page(60 * 2))
    # @method_decorator(vary_on_headers("Authorization",))
    def get(self, request):
        print("user:100", cache.get("user:100"))
        my_multiply.delay(2, 6)
        qs = Category.objects.filter(user=request.user).order_by("-created_at")
        qs = Category.objects.all().order_by("-created_at")
        serializer = CategoryListSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoryListSerializer(data=request.data, context={"user": request.user})  
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"status": "success", "message": "ijad shod"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"status": "error", "error_message": "hamchin category ghablan dashti"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)


class TodoList(APIView):

    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request):
        qs = Todo.objects.all().filter(category__user=request.user)
        cache.set("user:100", qs, 100)
        serializer = TodoListSerializer(qs, many=True)
        print("request..accepted_renderer ", request.accepted_renderer)
    
        return Response(serializer.data)
    
    def post(self, request: Request):
        serializer = TodoListSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return super().get_queryset().filter(category__user=self.request.user)



class PostInstaView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = PostInstagrami.objects.select_related("user")
        serilizer = PostInstagramiListSerializer(qs, many=True)
        return Response(serilizer.data)
    
    def post(self, request):
        serializer = PostInstagramiListSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostInstagramiViewSet(viewsets.ViewSet):
    
#     permission_classes = [permissions.IsAuthenticated]

#     def list(self, request):
#         print("hello list")
#         queryset = PostInstagrami.objects.select_related("user")
#         serializer = PostInstagramiSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         print("hello detail")
#         queryset = PostInstagrami.objects.select_related("user")
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = PostInstagramiSerializer(post)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = PostInstagramiSerializer(data=request.data, context={"user": request.user})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# TODO: 1. slugfield retrieve, 2. list and retrieve have differnet serializer,
class PostInstagramiViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = PostInstagrami.objects.select_related("user")
    lookup_field = "slug"

    def retrieve(self, request: HttpRequest, *args, **kwargs):
        if request.user.has_perm("app.gozaresh_kardan"):
            return super().retrieve(request, *args, **kwargs)
        else:
            raise Exception("dari vari Moein")

    def get_serializer_class(self):
        if self.action == "list" or self.action == "create":
            return PostInstagramiListSerializer
        else:
            return PostInstagramiDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
    
    @action(detail=False, methods=["GET"], url_path="post-jadid", url_name="post-jadid")
    def recent_posts(self, request):
        recent_posts_ = PostInstagrami.objects.all().order_by('-created_at')[:3]
        serializer = PostInstagramiListSerializer(recent_posts_, many=True, context={"request": request})
        return Response(serializer.data)


class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SendSms(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        result = random.randint(1000, 9999)
        cache.set(request.user.username, result, 120)
        subject = 'code for login'
        message = f'code: {result}'
        email_from = "ashkan.ekbatan90@gmail.com"
        recipient_list = ['naghavi.mohamad68@gmail.com',]
        async_send_mail.delay(subject, message, email_from, recipient_list)
        return Response({"status": "success", "code": result})

    def post(self, request):
        cache_code_ = cache.get(request.user.username)
        send_code_ = request.data.get("code")
        if send_code_:
            if send_code_== cache_code_:
                return Response({"status": "success"})
            else:
                return Response({"status": "error", "error_message": "code expire shode ya eshteb zadi, mojadad talash kon"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error", "error_message": "code field is required"}, status=status.HTTP_400_BAD_REQUEST)
            

class GherUmadan(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.has_perm("app.ide_soroush")


class Kabareh(APIView):

    permission_classes = [permissions.IsAuthenticated , GherUmadan]

    def get(self, request):
        return Response({"status": "baba karam"})