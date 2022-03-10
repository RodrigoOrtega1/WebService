import requests

# Clase que implementa llamadas al api de openweathermap

# Metodo que toma una cadena y ve si esta compuesta de numeros
def check_str(str):
    ls = str.lstrip("-").split(".")
    result = all(n.isdigit() for n in ls) and len(ls) <= 2
    return result

# #Metodo que pide una latitud y longitud y regresa la respuesta del API de openweathermap
def peticion(lat, lon):
    if type(lat) is not str or type(lon) is not str:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")
    if check_str(lat) == False or check_str(lon) == False:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")

    llave = "" #Colocar una key al API de openweathermap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}&units=metric"
    respuesta = requests.get(url).json()

    nombre = respuesta['name']
    clima = respuesta['weather'][0]['main']
    temperatura = respuesta['main']['temp']

    return f"{nombre} clima: {clima} temp: {temperatura}°C"