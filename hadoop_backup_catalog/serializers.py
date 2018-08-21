from rest_framework import serializers
from .models import metadata, applications, backupsets, backupoperations, backupfile_exceptions, backuparchives_raw, \
    backuparchives, exclusion_list, backup_recovery


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
        fields = '__all__'


class BackupoperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = backupoperations
        fields = '__all__'


class BackupfileExceptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = backupfile_exceptions
        fields = '__all__'


class BackuparchivesRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = backuparchives_raw
        fields = '__all__'


class BackuparchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = backuparchives
        fields = '__all__'


class ExclusionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = exclusion_list
        fields = '__all__'


class BackupRecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = backup_recovery
        fields = '__all__'


class UsernameFromAppnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = applications
        fields = '__all__'


class BackupReportsSerializer(serializers.Serializer):
    appid = serializers.IntegerField()
    last_backup_timestamp = serializers.DateTimeField()
    num_files = serializers.IntegerField()


class BackupReportsVolumeSerializer(serializers.Serializer):
    appid = serializers.IntegerField()
    last_backup_timestamp = serializers.DateTimeField()
    file_size = serializers.IntegerField()


class AdminReportsOperationsSerializer(serializers.Serializer):
    appid = serializers.IntegerField()
    last_backup_timestamp = serializers.DateTimeField()
    num_files = serializers.IntegerField()
    appname = serializers.CharField()



