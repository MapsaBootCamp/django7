from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser

from app.serializers import TodoDetailSerializer, TodoListSerializer
from app.models import Todo


class TodoList(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request):
        qs = Todo.objects.all()
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

