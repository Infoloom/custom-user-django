from django.urls import include, path

from .views import RegistrationAPI, LoginAPI, UserAPI
from rest_auth.views import LogoutView

urlpatterns = [
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/user/', UserAPI.as_view()),
    path('auth/logout/', LogoutView.as_view()),
]