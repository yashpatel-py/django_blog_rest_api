from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("login/", obtain_auth_token, name="login"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("register/", views.user_register_view, name="register"),
]
