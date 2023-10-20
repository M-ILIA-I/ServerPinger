import socket
import multiprocessing
from django.db.utils import load_backend
from django.db import models, IntegrityError, connections
from .response_time_decorator import measure_time
from ..models import ResponseModel
import psycopg2


def ping(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return True
    except socket.gaierror as e:
        return False
    

def save_result(adress):
    decorated_responce_function = measure_time(ping)
    
    result, delay_time = decorated_responce_function(adress)

    return result, delay_time
   

def multiptocessing_ping(lst_adresses):
    with multiprocessing.Pool(processes=len(lst_adresses)) as pool: 
        result = pool.map(save_result, lst_adresses)

    for i in range(len(lst_adresses)):
        responce_model = ResponseModel.objects.get(adress=lst_adresses[i])
        if result[i][0]==False:
            responce_model.responce_time = -1
            continue
        else:
            responce_model.responce_time = result[i][1]
            responce_model.save()
    
            

