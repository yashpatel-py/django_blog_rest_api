from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# class BlogListCreatePagination(PageNumberPagination):
#     page_size = 1
#     # page_query_param = 'p'
#     page_size_query_param = "size"
#     max_page_size = 50

# class BlogListCreatePagination(LimitOffsetPagination):
#     default_limit = 2
#     max_limit = 10
#     limit_query_param = "limit"
#     offset_query_param = "start"

class BlogListCreatePagination(CursorPagination):
    page_size = 2
    ordering = "post_date"
    