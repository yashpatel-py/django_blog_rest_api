from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets

from django.shortcuts import get_object_or_404


# class BlogViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Blog.objects.filter(is_public=True)
#         serializer = BlogSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = Blog.objects.filter(is_public=True)
#         blog_list = get_object_or_404(queryset, pk=pk)
#         serializer = BlogSerializer(blog_list)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = BlogSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         blog.delete()
#         return Response({"Message": "Your blog has been deleted"}, status=status.HTTP_204_NO_CONTENT)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(is_public=True)
    serializer_class = BlogSerializer

















# class CategoryListView(APIView):
#     def get(self, request):
#         all_category = Category.objects.all()
#         serializers = CategorySerializer(all_category, many=True, context={'request': request})
#         return Response(serializers.data)

# class CategoryDetailView(APIView):
#     def get(self, request, pk):
#         single_category = Category.objects.get(pk=pk)
#         serializers = CategorySerializer(single_category, context={'request': request})
#         return Response(serializers.data)

# # GET, POST
# class BlogListView(APIView):
#     def get(self, request):
#         all_blogs = Blog.objects.filter(is_public=True)
#         serializer = BlogSerializer(all_blogs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # GET, PUT, DELETE 
# class BlogDetailView(APIView):
#     def get(self, request, pk):
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_200_OK)

# # ------------------ generic view
# class BlogListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class BlogDetailGenericView(mixins.RetrieveModelMixin, 
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             generics.GenericAPIView):

#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'slug'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Concrete Views
# class BlogCreateCon(generics.CreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogListcon(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogRetrievecon(generics.RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'slug'

# class BlogDestroyCon(generics.DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogUpdateCon(generics.UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogretrieveUpdateCon(generics.RetrieveUpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogRetrieveDestroyCon(generics.RetrieveDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogListCreateApiView(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogRUDApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer