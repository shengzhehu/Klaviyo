import requests
import json

def get_weather_data(city):

    cur_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    tomr_url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    cur_city_weather = requests.get(cur_url.format(city)).json() #request the API data and convert the JSON to Python data types
    tomr_city_weather = requests.get(tomr_url.format(city)).json()

    cur_weather = {
        'city' : city,
        'temperature' : cur_city_weather['main']['temp'],
        'description' : cur_city_weather['weather'][0]['description'],
        'icon' : cur_city_weather['weather'][0]['icon']
    }

    tomr_weather = {
        'city' : city,
        'temperature' : tomr_city_weather['list'][0]['main']['temp'],}
    #     'description' : tomr_city_weather['weather'][0]['description'],
    #     'icon' : tomr_city_weather['weather'][0]['icon']
    # }

    return cur_weather, tomr_weather #returns the index.html template
