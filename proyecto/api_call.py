import requests

# Clase que implementa llamadas al api de openweathermap

# Metodo que toma una cadena y ve si esta compuesta de numeros
def check_str(str):
    # Quita el simbolo de menos y divide la cadena en dos a partir del punto
    ls = str.lstrip("-").split(".")
    result = all(n.isdigit() for n in ls) and len(ls) <= 2
    return result

# #Metodo que pide una latitud y longitud y regresa la respuesta del API de openweathermap
def peticion(lat, lon):
    # Checa si el tipo de la entrada es una string
    if type(lat) is not str or type(lon) is not str:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")
    # Checa que la cadena solo tenga valores numericos
    if check_str(lat) == False or check_str(lon) == False:
        raise ValueError("Latitud y longitud deben ser cadenas de numeros")

    llave = "ccfde2d4fa36e3a5ea238785c052590d" #Colocar una key al API de openweathermap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}&units=metric"
    respuesta = requests.get(url).json()

    nombre = respuesta['name']
    clima = respuesta['weather'][0]['main']
    temperatura = respuesta['main']['temp']

    return f"{nombre} clima: {clima} temp: {temperatura}°C"
     # + '\n' + f"clima: {clima}"+ '\n' + f"temp: {temperatura}°C"

# dic = {}
# dic.update({peticion("19.3371","-99.566") : peticion("25.7785","-100.107")})
# print(dic)
# print(peticion("19.3371","-99.566"))
# print(peticion("25.7785","-100.107"))
