'''Escreva um programa que use a API do Google Maps para obter coordenadas (latitude e longitude) a partir de um endereço especificado.'''
import requests

def get_coordinates(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"Error: {data['status']}")
    else:
        print(f"Failed to connect to the API, status code: {response.status_code}")

# Substitua 'YOUR_API_KEY' pela sua chave real da API do Google Maps
API_KEY = 'YOUR_API_KEY'
address = "1600 Amphitheatre Parkway, Mountain View, CA"
latitude, longitude = get_coordinates(address, API_KEY)
print(f"Coordinates for '{address}': Latitude = {latitude}, Longitude = {longitude}")

'''Escreva um programa que usa a API do OpenWeatherMap para obter a previsão do tempo atual em uma cidade especificada.'''
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Para temperatura em Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Temperatura atual em {city_name}: {weather_data['main']['temp']}°C")
        print(f"Descrição do clima: {weather_data['weather'][0]['description']}")
    else:
        print(f"Erro: {response.status_code} - {response.json()['message']}")

# Substitua 'your_api_key' pela sua chave de API do OpenWeatherMap
api_key = 'your_api_key'
city_name = input("Digite o nome da cidade: ")
get_weather(city_name, api_key)