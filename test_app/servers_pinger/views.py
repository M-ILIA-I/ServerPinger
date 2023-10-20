from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import redirect
from .services import pinger
from .models import ResponseModel
import requests


class MainPage(TemplateView):
    template_name = 'main_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_adress_list"] = ResponseModel.objects.all()
        context["UPDATE_FREQUENCY"] = settings.UPDATE_FREQUENCY

        return context


    def get(self, request, *args, **kwargs):
        adresses = ResponseModel.objects.values('adress')
        pinger.multiptocessing_ping(list(adresses.values_list('adress', flat=True)))

        return render(request,'main_page.html', self.get_context_data(**kwargs))    


class ChartPage(TemplateView):
    template_name = 'chart_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                'values': [12, 19, 3, 5, 2, 3]}
        context['servers'] = requests.get('http://localhost:8000/servers/').json()
        context['data'] = data
        return context
    

    
