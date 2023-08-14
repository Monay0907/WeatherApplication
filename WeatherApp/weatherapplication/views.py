from django.shortcuts import render
import requests
def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15,2)
def search(request):
    if request.method == 'POST':
        city=request.POST.get('city')
        api_key='482675b24ebe2b418e13d593167e1ee0'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response=requests.get(url)
        data=response.json()
        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'temperature': kelvin_to_celsius(data['main']['temp']),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = None

        return render(request, 'search.html', {'weather_data': weather_data})

    return render(request, 'search.html')