from rest_framework import serializers
from servers_pinger.models import ResponseModel

class ResponceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = ['adress', 'responce_time', 'ping_time']