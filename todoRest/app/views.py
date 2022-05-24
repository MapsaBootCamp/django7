from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token

from app.serializers import TodoDetailSerializer, TodoListSerializer
from app.models import Todo


class TodoList(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = Todo.objects.all()
        serializer = TodoListSerializer(qs, many=True)
        return Response(serializer.data)


class TodoDetail(APIView):

    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data)


for user in User.objects.all():
    Token.objects.get_or_create(user=user)