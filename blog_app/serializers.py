from rest_framework import serializers
from blog_app.models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)
    # category = serializers.StringRelatedField(many=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True,
    #     view_name='blog_detail'
    # )
    # category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    class Meta:
        model = Category
        exclude = ['id',]

# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     category_name = serializers.CharField()
#     category = BlogSerializer(many=True, read_only=True)
#     # category = serializers.StringRelatedField(many=True)
#     # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # category = serializers.HyperlinkedRelatedField(
#     #     many=True, 
#     #     read_only=True,
#     #     view_name='blog_detail'
#     # )
#     # category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
#     class Meta:
#         model = Category
#         fields = '__all__'