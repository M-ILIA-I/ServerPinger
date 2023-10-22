from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import redirect
from .services import pinger
from .models import ResponseModel
import requests
import logging


logger = logging.getLogger('mailings')

class MainPage(TemplateView):
    template_name = 'main_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_adress_list"] = ResponseModel.objects.all()
        context["UPDATE_FREQUENCY"] = settings.UPDATE_FREQUENCY
        return context

    def get(self, request, *args, **kwargs):
        adresses = ResponseModel.objects.values('adress').distinct()
        lst_adresses = list(adresses.values_list('adress', flat=True))
        
        if len(lst_adresses) > 1:
            pinger.multiptocessing_ping(lst_adresses)
            logger.info("Servers was pinged multiprocessing")

        elif len(lst_adresses) == 1:
            pinger.single_pick(lst_adresses[0])
            logger.info("Servers was pinged single")

        return render(request,'main_page.html', self.get_context_data(**kwargs))    


class ChartPage(TemplateView):
    template_name = 'chart_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        request_data = requests.get('http://localhost:8000/servers/').json()
        context["dataset"] = request_data

        logger.info("data was recieved from drf")
            
        return context
    

    
