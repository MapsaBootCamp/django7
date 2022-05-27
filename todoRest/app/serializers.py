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
        fields = ["id", "title", "category"]

class TodoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        exclude = ["id"]