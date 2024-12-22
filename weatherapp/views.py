import datetime
import requests
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'Kathmandu')
    else:
        city = 'Kathmandu'

    # Call the weather API with proper parameters
    url = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {
        'q': city,
        'appid': 'e2c548d4811226ee99039d6e009c588a',
        'units': 'metric'
    }

    response = requests.get(url, params=PARAMS)
    data = response.json()

    # Check if the response contains an error (city not found)
    if response.status_code != 200 or data.get('cod') != 200:
        error_message = "City not found. Please enter a valid city name."
        return render(request, 'weatherapp/index.html', {'error_message': error_message, 'city': city})


    # Extract relevant data
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    coordinates = f"Lat: {data['coord']['lat']}, Lon: {data['coord']['lon']}"
    country_code = data['sys']['country']
    day = datetime.date.today()


    return render(request, 'weatherapp/index.html', {
        'city': city,
        'description': description,
        'icon': icon,
        'temp': temp,
        'coordinates': coordinates,
        'country_code': country_code,
        'day': day
    })
