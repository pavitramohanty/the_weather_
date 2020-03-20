import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f3cb19282c7c0636cccf91529010e64b'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    Citys = City.objects.all()

    weather_data = []

    for city in Citys:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temprature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'wind' : r['wind']['speed'],
        }
        weather_data.append(city_weather)
    
    context = {'weather_data':weather_data, 'form' : form}
    return render(request, 'weather/index.html', context)
