from rest_framework import serializers

from app.models import Todo


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ["id", "title", "category"]

class TodoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        exclude = ["id"]