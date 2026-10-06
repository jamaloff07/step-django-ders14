from rest_framework import serializers

from blog.models import Category, Post, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id", "title", "author", "category", "content", "tags",
            "is_published", "is_featured", "views", "created_at",
        )
        read_only_fields = ("id", "views", "created_at")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "description")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "slug")
