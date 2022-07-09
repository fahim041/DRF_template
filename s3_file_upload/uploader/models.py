from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
# Create your models here.


class Uploader(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=500, upload_to="pic/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Store(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(storage=S3Boto3Storage(
        bucket_name='drf-uploader-store'), max_length=500, upload_to="pic/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Files(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(storage=S3Boto3Storage(
        bucket_name='drf-uploader-us'), max_length=500, upload_to="file/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
