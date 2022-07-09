from rest_framework import serializers
from .models import Files, Store, Uploader


class UploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploader
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'
