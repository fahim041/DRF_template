from django.urls import path

from .views import play

urlpatterns = [
    path('', play, name='play')
]
