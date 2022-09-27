from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    
    data = {
        "Blogs": list(blogs.values())
    }
    return JsonResponse(data)

def blog_detail(request, pk):
    blogs = Blog.objects.get(pk=pk)

    data = {
        'name': blogs.name,
        'description': blogs.description,
        'slug': blogs.slug,
    }
    return JsonResponse(data)