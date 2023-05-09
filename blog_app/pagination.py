from rest_framework.pagination import PageNumberPagination

class BlogListCreatePagination(PageNumberPagination):
    page_size = 1
    # page_query_param = 'p'
    page_size_query_param = "size"
    max_page_size = 50