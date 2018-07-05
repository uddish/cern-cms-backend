from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import metadata, applications, backupsets, backupoperations, backupfile_exceptions,backuparchives_raw, backuparchives, exclusion_list
from .serializers import MetadataSerializer, ApplicationsSerializer, BackupsetsSerializer, BackupoperationsSerializer, BackupfileExceptionsSerializer, BackuparchivesRawSerializer, BackuparchivesSerializer, ExclusionListSerializer


# Metadata api
class MetadataList(APIView):

    def get(self, request):
        data = metadata.objects.all()
        serializer = MetadataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


#Applications api
class ApplicationList(APIView):

    def get(self, request):
        data = applications.objects.all()
        serializer = ApplicationsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BackupsetsList(APIView):

    def get(self, request):
        data = backupsets.objects.all()
        serializer = BackupsetsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BackupoperationsList(APIView):

    def get(self, request):
        data = backupoperations.objects.all()
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


class BackuparchivesRawList(APIView):

    def get(self, request):
        data = backuparchives_raw.objects.all()
        serializer = BackuparchivesRawSerializer(data, many=True)
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

    def get(self, request):
        data = exclusion_list.objects.all()
        serializer = ExclusionListSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass