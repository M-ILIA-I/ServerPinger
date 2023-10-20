from django.db import models

class ResponseModel(models.Model):
    adress = models.CharField(max_length=100)
    responce_time = models.FloatField(null=True, blank=True, default=0)
    
    def __str__(self) -> str:
        return self.adress
    

