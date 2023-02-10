from rest_framework import serializers
from blog_app.models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        exclude = ['id',]