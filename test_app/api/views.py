from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from servers_pinger.models import ResponseModel
from .serializers import ResponceModelSerializer

class ResponceList(APIView):
    def get(self, request):
        queryset = ResponseModel.objects.all()
        serializer_class = ResponceModelSerializer(instance=queryset, many=True)
        return Response(serializer_class.data)