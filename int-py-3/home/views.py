from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    city=request.GET.get('city','Lucknow')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9d69ebde5d7b886a4c8df538f7d40dd0'
    data=requests.get(url).json()
    payload={
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature':data['main']['temp'],
        'celsius_temperature':int(data['main']['temp']-273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description': data['weather'][0]['main'],
    }
    context={'data':payload}
    print(context)

    return render(request,'home.html',context)
