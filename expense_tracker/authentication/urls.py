from django.urls import path
from .views import RegisterView, VerifyEmail

from rest_framework import permissions

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify', VerifyEmail.as_view(), name='email-verify'),

]
