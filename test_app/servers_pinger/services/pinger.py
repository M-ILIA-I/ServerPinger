import socket
import multiprocessing
from .response_time_decorator import measure_time
from ..models import ResponseModel
import datetime


def ping(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return True
    except socket.gaierror as e:
        return False
    

def get_responce_time(adress):
    decorated_responce_function = measure_time(ping)
    result, delay_time = decorated_responce_function(adress)

    return result, delay_time
   

def multiptocessing_ping(lst_adresses):
    with multiprocessing.Pool(processes=len(lst_adresses)) as pool: 
        result = pool.map(get_responce_time, lst_adresses)

    for i in range(len(lst_adresses)):
        responce_model = ResponseModel()
        if result[i][0]==False:
            continue
        else:
            responce_model.adress = lst_adresses[i]
            responce_model.responce_time = result[i][1]
            responce_model.ping_time = str(datetime.datetime.now().hour)
            responce_model.save()

        

def single_pick(adress):
    res, time = get_responce_time(adress)
    responce_model = ResponseModel()
    responce_model.adress = adress

    if res:
        responce_model.responce_time = time
        responce_model.ping_time = str(datetime.datetime.now().hour)
        responce_model.save()