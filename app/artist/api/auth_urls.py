from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from .views import LoginView

urlpatterns = [
    path('refresh/', refresh_jwt_token),     # api/auth/refresh/
    path('login/', LoginView.as_view()),     # api/auth/login/
]
