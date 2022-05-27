from django.shortcuts import get_object_or_404
from rest_framework import serializers

from app.models import Todo, Category


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']

    def create(self, validated_data):
        name = validated_data.get("name")
        return Category.objects.create(user=self.context["user"], name=name)


class CategoryDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class TodoListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ["id", "title", "category", "due_date"]
        extra_kwargs = {
            'due_date': {'write_only': True}
        }

    def create(self, validated_data):
        category = validated_data.pop("category")
        category_obj = get_object_or_404(Category, user=self.context["user"], pk=category.id)
        return Todo.objects.create(**validated_data, category=category_obj)

class TodoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        exclude = ["id"]