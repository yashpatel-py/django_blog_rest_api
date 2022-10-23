from django.contrib import admin
from .models import Blog, BlogComment, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'post_date', 'is_public')
    list_display_links = ('id', 'blog_title')
    search_fields = ('blog_title',)
    list_per_page = 10
    list_editable = ("is_public",)
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Category)
