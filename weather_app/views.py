from django.shortcuts import render
from weather_app.weather_service import get_weather_data

def weather_view(request):
    weather_data = None

    if request.method =='POST':
        city = request.POST.get('city', '')
        weather_data = get_weather_data(city)

    return render(request, 'weather.html', {'weather_data': weather_data})  

