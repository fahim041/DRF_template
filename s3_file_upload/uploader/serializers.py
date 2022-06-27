from rest_framework import serializers
from .models import Uploader


class UploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploader
        fields = '__all__'
