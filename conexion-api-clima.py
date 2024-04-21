import requests  

"""tengo un problema que solucionar en mi pc con el " request, algo que quedó corrupto del pip""""
ciudad = "new york "#cambiar segun gusto
api_key = "e7f5bc03ec11295edfa831ccfe3b17aa"

"""revisas el pip install para poder avanzar"""

url = f"http://api.openweathermap.org/2.5/weather?q=
{ciudad}&apiid={api_key}"

respuesta= requests.get(url).json()

if "main" in respuesta:
    clima = respuesta ["weather"][0]["description"]
    temperatura= respuesta ["main"]["temp"]
    humedad= respuesta["main"]["pressure"]
    presion= respuesta["main"]["pressure"]
    viento= respuesta["wind"]["speed"]

    print(f"clima actual en {ciudad}")
    print(f"descripcion del clima: {ciudad}")
    print(f"temperura F {temperatura}")
    print(f"humedad: {ciudad}")
    print(f"presion: {ciudad}")
    print(f"viento: {ciudad}")