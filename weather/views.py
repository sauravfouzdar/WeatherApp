from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests
from . models import City 
from . forms import CityForm

def home(request):
   
    #url = 'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=d3f5cb20306201428b26258023940762'
    
    
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6177a4dc167655f2d0c1a071f32c3bad'
    #city = 'New York'
   
    form = CityForm()
    if request.method == 'POST':
       form = CityForm(request.POST)
       if form.is_valid():
          form.save()
        
    
    city_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        city_data.append(weather)

    context = {'city_data': city_data, 'form':form} 

    return render(request, 'home.htm', context)

def remove_city(request, city_name):
    City.objects.filter(nameOfCity=city_name).delete()
    
    return redirect('home')




