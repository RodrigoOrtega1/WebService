from dotenv import load_dotenv
import os
import requests

def es_num(str):
    '''
    Toma una cadena
    Regresa True si esta compuesta solamente de numeros
    :param str: Una cadena
    :return result: True si str esta compuesta de numeros
    '''
    ls = str.lstrip("-").split(".")
    return all(n.isdigit() for n in ls) and len(ls) <= 2

def peticion(lat, lon):
    '''
    Toma dos coordenadas
    Regresa el clima en las coordenadas
    :param lat: Una cadena con la latitud
    :param lon: Una cadena con la longitud
    :return: Una cadena con el clima en las coordenadas dadas
    '''
    load_dotenv()
    if type(lat) is not str or type(lon) is not str:
        raise ValueError("Latitud y longitud deben ser cadenas exclusivamente de numeros")
    if es_num(lat) == False or es_num(lon) == False:
        raise ValueError("Latitud y longitud deben ser cadenas exclusivamente de numeros")

    llave = os.getenv("llave")
    if (llave and not llave.isspace()):
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}&units=metric"
    else:
        raise ValueError("El programa debe tener una llave de OpenWeatherMap valida")

    respuesta = requests.get(url).json()
    nombre = respuesta['name']
    clima = respuesta['weather'][0]['main']
    temperatura = respuesta['main']['temp']

    return f"{nombre}|clima:{clima}|temp:{temperatura}°C"
