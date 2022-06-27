from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import Uploader
from .serializers import UploaderSerializer

# Create your views here.


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Uploader.objects.all()
    serializer_class = UploaderSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
