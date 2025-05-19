from django.urls import path
from .views import UserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/signup/', UserCreateView.as_view(), name='signup'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
]