from rest_framework.throttling import UserRateThrottle

class BlogListCreateViewThrottle(UserRateThrottle):
    scope = "blog-list"