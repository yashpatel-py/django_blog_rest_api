from django.contrib import admin
from .models import Blog, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'post_date', 'is_public')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author')
    list_per_page = 1
    list_editable = ("is_public",)
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
