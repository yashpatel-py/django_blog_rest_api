from rest_framework import serializers
from blog_app.models import Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.StringRelatedField(read_only=True)
    description = serializers.CharField()
    post_date = serializers.DateTimeField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)