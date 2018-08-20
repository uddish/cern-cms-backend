from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .pagination import BackupArchiveRawPagination, BackupSetsPagination, BackupOperationsPagination
from rest_framework.generics import ListAPIView
from rest_framework import status


# Metadata api
class MetadataList(APIView):

    def get(self, request):
        data = metadata.objects.all()
        serializer = MetadataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# Applications api
class ApplicationList(APIView):

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = applications.objects.filter(appid=appid[0].get('appid'))
        serializer = ApplicationsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class UsernameFromApplication(APIView):

    def get(self, request, *args, **kwargs):
        appname = kwargs['appname']
        appid = applications.objects.filter(appname=appname).values('appid')
        data = applications.objects.filter(appid=appid[0].get('appid'))
        serializer = UsernameFromAppnameSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class BackupsetsList(APIView):

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = backupsets.objects.filter(appid=appid[0].get('appid'))
        serializer = BackupsetsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BackuparchivesRawList(ListAPIView):
    pagination_class = BackupArchiveRawPagination
    serializer_class = BackuparchivesRawSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = backuparchives_raw.objects.filter(appid=appid[0].get('appid'))
        return data


class BackupoperationsList(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = backupoperations.objects.order_by('-last_backup_timestamp').filter(appid=appid[0].get('appid'))
        serializer = BackupoperationsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class LatestBackupOperation(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = backupoperations.objects.filter(appid=appid[0].get('appid'), status='COMPLETED').order_by('-last_backup_timestamp')[:1]
        serializer = BackupoperationsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BackupfileExceptionsList(APIView):

    def get(self, request):
        data = backupfile_exceptions.objects.all()
        serializer = BackupfileExceptionsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BackuparchivesList(APIView):

    def get(self, request):
        data = backuparchives.objects.all()
        serializer = BackuparchivesSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ExclusionList(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = exclusion_list.objects.filter(appid=appid[0].get('appid'))
        serializer = ExclusionListSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BackupRecovery(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        data = backup_recovery.objects.filter(username=username).order_by('-requested_timestamp')
        serializer = BackupRecoverySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BackupRecoverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BackupReportsNoOfFiles(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = backupoperations.objects.raw('select bo.id, bo.appid,bo.boid,last_backup_timestamp,sum(num_files) as num_files '
                                            'from backupoperations bo, backupsets bs where bo.appid = %s and bo.appid=bs.appid and bo.boid=bs.boid '
                                            'group by bo.id,bo.appid,bo.boid,last_backup_timestamp, num_files order by last_backup_timestamp desc', [appid[0].get('appid')])[:30]
        serializer = BackupReportsSerializer(data, many=True)
        return Response(serializer.data)


class BackupReportsVolume(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        appid = applications.objects.filter(username=username).values('appid')
        data = backupoperations.objects.raw('select bo.id, bo.appid,bo.boid,last_backup_timestamp,sum(file_size) as file_size '
                                            'from backupoperations bo, backuparchives_raw ba '
                                            'where bo.appid = %s and bo.appid=ba.appid and bo.boid=ba.boid '
                                            'group by bo.id, bo.appid,bo.boid,last_backup_timestamp, file_size, file_size', [appid[0].get('appid')])[:30]
        serializer = BackupReportsVolumeSerializer(data, many=True)
        return Response(serializer.data)

