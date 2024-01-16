import requests
def get_weather(state_code, city):
    api_key = '68c43d91d9dd320c3b1384107916c06c'
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},+1&limit=1&appid={api_key}'
    response = requests.get(url)
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    weather = response.json()
    t = process_weather(weather)
    return t

def process_weather(weather):
    current_weather = {
        'main': weather['weather'][0]['main'],
        'description': weather['weather'][0]['description'],
        'temp': weather['main']['temp'] * 1.8 - 459.67,
        'feels_like': weather['main']['feels_like'] * 1.8 - 459,
        'temp_min': weather['main']['temp_min'] * 1.8 - 459,
        'temp_max': weather['main']['temp'] * 1.8 - 459,
        'wind': weather['wind']['speed']
    }
    print(current_weather)
    return current_weather