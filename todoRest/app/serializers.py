from attr import fields
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.contrib.auth import get_user_model

from rest_framework import serializers

from app.models import FollowerTable, FollowerUser, PostInstagrami, Todo, Category

User = get_user_model()


# HyperlinkedModelSerializer ----> ListView
# ModelSerializer ----> DetailView

def check_name(value):
    if 'mapsa' not in value:
        raise serializers.ValidationError('name field must have mapsa as prefix.')

class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    
    capital_name = serializers.SerializerMethodField()
    # name = serializers.CharField(validators=[check_name])
    
    def validate_name(self, val):
        if 'mapsa' not in val:
            raise serializers.ValidationError('name field must have mapsa as prefix.')
        return val
    
    # def validate(self, data):
    #     if 'mapsa' not in data.get("name"):
    #         raise serializers.ValidationError('name field must have mapsa as prefix.')
    #     return data

    class Meta:
        model = Category
        fields = ['url', 'name', 'capital_name']
        
    def create(self, validated_data):
        name = validated_data.get("name")
        return Category.objects.create(user=self.context["user"], name=name)
    
    def get_capital_name(self, obj):
        if obj.name:
            return obj.name.upper()


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


class CustomCharField(serializers.Field):

    def to_representation(self, value):
        return f"salam {value}"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "first_name"]


class PostInstagramiListSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     read_only=True,
    #     view_name='posts-detail',
    #     lookup_field= 'slug'
    # )
    class Meta:
        model = PostInstagrami
        fields = ["url", "caption", "img"]
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
    
    def create(self, validated_data):
        return PostInstagrami.objects.create(user=self.context["user"], **validated_data)


class PostInstagramiDetailSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    username = CustomCharField(source="user.username", read_only=True)

    class Meta:
        model = PostInstagrami
        fields = "__all__"

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def get_days_since_created(self, obj):
        return (now().date() - obj.created_at).days

class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FollowerUser
        exclude = ["follower"]
        extra_kwargs = {
            "status": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        darkhast_dahande = self.context["user_darkhast_dahande"]
        darkhast_shavande = validated_data["user"].follwer_table
        return FollowerUser.objects.create(follower=darkhast_shavande, user=darkhast_dahande, status="p")

class FollowTableSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = FollowerTable
        fields = ["user"]


class FollowingSerializer(serializers.ModelSerializer):
    following = FollowTableSerializer(read_only=True, source="follower")

    class Meta:
        model = FollowerUser
        fields = ["following"]


class FollowerTest(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    followers = FollowerSerializer(many=True)

    class Meta:
        model = FollowerTable
        fields = ["user", "followers"]