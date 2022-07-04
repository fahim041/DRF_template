from django.db import models

# Create your models here.


class Uploader(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=500, upload_to="pic/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
