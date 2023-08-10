from django.urls import path
from .views import UserLoginApiView, UserRegisterAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('login/', UserLoginApiView.as_view()),
]
