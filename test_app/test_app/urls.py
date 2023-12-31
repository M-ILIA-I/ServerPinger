"""
URL configuration for test_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from servers_pinger.views import MainPage, ChartPage
from api.views import ResponceList
from servers_pinger.models import ResponseModel
from servers_pinger.services import pinger
from time import sleep
from . import settings
import asyncio
from asgiref.sync import sync_to_async


async def png():
    while True:
        adresses = await sync_to_async(ResponseModel.objects.values)('adress')
        # await sync_to_async(pinger.multiptocessing_ping(list(adresses.values_list('adress', flat=True))))
        await asyncio.sleep(settings.UPDATE_FREQUENCY)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', MainPage.as_view(), name='main-page'),
    path('servers/', ResponceList.as_view(), name='responce-list'),
    path('chart/', ChartPage.as_view(), name='cgart-page'),
]

# loop = asyncio.new_event_loop()
# loop.run_until_complete(png())
#asyncio.run(png())