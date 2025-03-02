import requests
from django.conf import settings

def get_weather_data(city):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error Fetching Weather: {e}")
        return None
    

