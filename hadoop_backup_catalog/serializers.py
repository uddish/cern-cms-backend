from rest_framework import serializers
from .models import metadata, applications, backupsets, backupoperations, backupfile_exceptions,backuparchives_raw, backuparchives, exclusion_list

class MetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = metadata
        fields = '__all__'


class ApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = applications
        fields = '__all__'


class BackupsetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = backupsets
        field = '__all__'


class BackupoperationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = backupoperations
        field = '__all__'


class BackupfileExceptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = backupfile_exceptions
        field = '__all__'


class BackuparchivesRawSerializer(serializers.ModelSerializer):

    class Meta:
        model = backuparchives_raw
        field = '__all__'


class BackuparchivesSerializer(serializers.ModelSerializer):

    class Meta:
        model = backuparchives
        field = '__all__'


class ExclusionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = exclusion_list
        field = '__all__'