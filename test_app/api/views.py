from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from servers_pinger.models import ResponseModel
from .serializers import ResponceModelSerializer
from django.db.models import Count, Avg
from servers_pinger.services import chart_data

class ResponceList(APIView):
    def get(self, request):

        result = []
        
        for i in range(24):
            buffer = []
            queryset = ResponseModel.objects.filter(ping_time=i).values('adress').annotate(avg=Avg('responce_time'))
            for i in queryset:
                buffer.append(i)
            result.append(buffer)
        
        count = ResponseModel.objects.values_list('adress').distinct().count()
        
        result = {"dataset":chart_data.get_datasets(result,count)}     
       
        return Response(result)