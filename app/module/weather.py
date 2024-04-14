import requests
import os

def get_weather_by_coordinates(lat, lon):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url=endpoint, params=parameters)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f'error {str(e)}'

if __name__ == '__main__':
    lat = 51.90224
    lon = -0.20256
    print(get_weather_by_coordinates(lat, lon))







