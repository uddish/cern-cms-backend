from rest_framework import serializers
from .models import metadata, applications

class MetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = metadata
        fields = '__all__'

class ApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = applications
        fields = '__all__'