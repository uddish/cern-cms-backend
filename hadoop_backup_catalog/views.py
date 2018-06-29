from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import metadata, applications
from .serializers import MetadataSerializer, ApplicationsSerializer


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
