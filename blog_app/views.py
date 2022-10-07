from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def blog_list(request):
    all_blogs = Blog.objects.filter(is_public=True)
    serializer = BlogSerializer(all_blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)