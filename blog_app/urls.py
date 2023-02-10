from django.urls import path, include
from . import views

urlpatterns = [
    path("blog_list/", views.BlogListCreateView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_list"),
]