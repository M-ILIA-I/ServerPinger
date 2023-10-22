from django.utils import timezone
from django.db import models
import logging
import datetime


logger = logging.getLogger('mailings')

class ResponseModel(models.Model):
    adress = models.CharField(max_length=100)
    responce_time = models.FloatField(null=True, blank=True, default=0)
    ping_time = models.CharField(default=str(datetime.datetime.now().hour), max_length=2)

    def save(self, *args, **kwargs):
        created = not self.pk  

        super(ResponseModel, self).save(*args, **kwargs)

        if created:
            logger.info('Created element with id %s', self.pk)

    def __str__(self) -> str:
        return self.adress
    

