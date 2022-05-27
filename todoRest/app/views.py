from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from matplotlib.style import context

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser

from app.serializers import CategoryDetailSerializer, CategoryListSerializer, TodoDetailSerializer, TodoListSerializer
from app.models import Category, Todo


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CategoryView(APIView):
    
    authentication_classes = [authentication.TokenAuthentication]
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

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request):
        qs = Todo.objects.all().filter(category__user=request.user)
        serializer = TodoListSerializer(qs, many=True)
        print("request..accepted_renderer ", request.accepted_renderer)
    
        return Response(serializer.data)
    
    def post(self, request: Request):
        print("request.data: ", request.data)
        print("request.query_param: ", request.query_params)
        print("request.parsers ", request.parsers)
        print("request.accepted_renderer ", request.accepted_renderer)
        print("request.accepted_media_type ", request.accepted_media_type)
        print("request.user: ", request.user)
        print("request.auth: ", request.auth)
        print("request.authicator: ", request.authenticators)
        # print("request.stream: ", request.stream)
        _response : Response = Response({"status": "OK"})
        print("------------------------------response")
        print("response.status_code: ", _response.status_code)
        return _response


class TodoDetail(APIView):

    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data)

