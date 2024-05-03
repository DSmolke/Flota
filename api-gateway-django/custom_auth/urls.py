from django.urls import path
from custom_auth.views import UserView, ActivationUserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('user/', UserView.as_view(), name=''),
    path('activate', ActivationUserView.as_view(), name=''),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
]