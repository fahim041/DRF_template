from rest_framework import serializers
from .models import Store, Uploader


class UploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploader
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
