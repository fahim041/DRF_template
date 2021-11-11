from django.urls import path
from .views import PasswordTokenCheckAPI, RegisterView, RequestPasswordResetEmail, TestSetNewPasswordAPIView, VerifyEmail, LoginAPIView, SetNewPasswordAPIView

from rest_framework import permissions

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify', VerifyEmail.as_view(), name='email-verify'),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name='request-reset-email'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('test-password-reset-complete/<uidb64>/<token>',
         TestSetNewPasswordAPIView.as_view(), name='test-password-reset-complete')
]
