import requests

def check_str(str):
    """
    Toma una cadena y ve si esta compuesta de numeros
    Params:
        str    - La cadena a checar
    Returns:
        result - True si si esta compuesta de numeros
    """
    ls = str.lstrip("-").split(".")
    result = all(n.isdigit() for n in ls) and len(ls) <= 2
    return result

def peticion(lat, lon):
    """
    Pide una latitud y longitud y regresa la respuesta del API de openweathermap
    Params:
        lat    - La latitud
        lon    - La longitud
    Returns:
        Una cadena con el nombre, clima y temperatura de las coordenadas
    """
    if type(lat) is not str or type(lon) is not str:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")
    if check_str(lat) == False or check_str(lon) == False:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")

    llave = "" #Colocar una key al API de openweathermap
    if (llave and not llave.isspace()):
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}&units=metric"
    else:
        raise ValueError("El programa debe tener una llave del API de openweathermap")

    respuesta = requests.get(url).json()

    nombre = respuesta['name']
    clima = respuesta['weather'][0]['main']
    temperatura = respuesta['main']['temp']

    return f"{nombre}|clima:{clima}|temp:{temperatura}°C"
