from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import Files, Store, Uploader
from .serializers import FileSerializer, StoreSerializer, UploaderSerializer

# Create your views here.


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Uploader.objects.all()
    serializer_class = UploaderSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
