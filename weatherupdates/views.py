import requests
import json
from datetime import datetime
from django.shortcuts import render


def index(request):
    try:
        if request.method == 'POST':
            API_KEY = '88c4d451fe655516f8630529f5730c9f'
            city = request.POST.get('city')

            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            response = requests.get(url).json()

            current_time = datetime.now()
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")

            city_weather_update = {
                'city': city,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'home.html', context)
    except Exception as e:
        return render(request, '404.html', {'error': str(e)})
