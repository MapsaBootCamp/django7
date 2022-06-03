from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

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
from app.serializers import CategoryDetailSerializer, CategoryListSerializer, PostInstagramiSerializer, TodoDetailSerializer, TodoListSerializer
from app.models import Category, PostInstagrami, Todo


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CategoryView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        qs = Category.objects.filter(user=request.user).order_by("-created_at")
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
        serilizer = PostInstagramiSerializer(qs, many=True)
        return Response(serilizer.data)
    
    def post(self, request):
        serializer = PostInstagramiSerializer(data=request.data, context={"user": request.user})
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
    serializer_class = PostInstagramiSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
    