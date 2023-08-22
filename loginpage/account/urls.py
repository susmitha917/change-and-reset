
from django.urls import path
from .views import *

urlpatterns = [
  path('register/',UserRegistrationView.as_view(), name='register'),
  path('login/',LoginView.as_view(), name='login'),
  path('profile/',ProfileView.as_view(), name='profile'),
  path('changepassword/',ChangePasswordView.as_view(), name='changepassword'),
  path('reset-password-email/',ResetPasswordEmailView.as_view(), name='reset-password-email'),
  path('reset-password/<uid>/<token>/',ResetPasswordView.as_view(), name='reset-password'),
]