from .models import Blog, Category, BlogComment
from .serializers import BlogSerializer, CategorySerializer, BlogCommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly



class CategoryListeCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # should be logged in to access this view
    # permission_classes = [IsAuthenticated] 
    
    # should be logged in and admin user
    # permission_classes = [IsAdminUser] 
    
    # should be logged to edit the details or you will have permission to view the data
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No category found'}, status=status.HTTP_404_NOT_FOUND)

class CategorydetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    liikup_field = 'id' # slug
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No blog Found'}, status=status.HTTP_404_NOT_FOUND)

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message':'No blogs found'}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer
    liikup_field = 'id' # slug
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No blog Found'}, status=status.HTTP_404_NOT_FOUND)

class BlogCommentListCreateView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    
    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)
    
    def perform_create(self, serializer):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        if BlogComment.objects.filter(blog=blog, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this blog'})
        serializer.save(author=self.request.user, blog=blog)