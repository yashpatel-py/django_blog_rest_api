from .models import Blog, Category, BlogComment
from .serializers import BlogSerializer, CategorySerializer, BlogCommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadonly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import BlogListCreatePagination


class CategoryListeCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
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
    permission_classes = [IsAdminOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No blog Found'}, status=status.HTTP_404_NOT_FOUND)

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    # UserRate & AnonRate Throttle
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    # ScopeRateThrottle
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'blog-list'

    # Custom Throttle
    # throttle_classes = [BlogListCreateViewThrottle]
    
    # Filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__category_name', 'is_public']
    search_fields = ['^blog_title', 'blog_description', 'category__category_name']
    # ordering_fields = ['Post date', 'category__category_name']
    
    # pagination
    pagination_class = BlogListCreatePagination

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
    permission_classes = [IsOwnerOrReadonly]
    
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
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)
    
    def perform_create(self, serializer):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        if BlogComment.objects.filter(blog=blog, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this blog'})
        serializer.save(author=self.request.user, blog=blog)

class BlogCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsOwnerOrReadonly]
    
    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(BlogComment, id = comment_id)
        
        blog_id = self.kwargs.get("blog_id")
        if comment.blog.id != blog_id:
            raise serializers.ValidationError({"Message": "This comment is not related to the requested blog"}, status=status.HTTP_401_UNAUTHORIZED)
        return comment
    
    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)