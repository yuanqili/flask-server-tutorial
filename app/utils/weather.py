import requests

from flask import current_app


def get_city_location_id(city):
    response = requests.get('https://geoapi.qweather.com/v2/city/lookup', params={
        'location': city,
        'key': current_app.config['HEFENG_KEY'],
    })
    if response.status_code != 200:
        print('request failed')

    data = response.json()
    if data['code'] != 200:
        print('query failed')

    location_id = data['location'][0]['id']
    return location_id


def get_city_7d_weather(city):
    location_id = get_city_location_id(city)
    response = requests.get('https://devapi.qweather.com/v7/weather/7d', params={
        'location': location_id,
        'key': current_app.config['HEFENG_KEY'],
    })
    if response.status_code != 200:
        print('request failed')

    data = response.json()
    if data['code'] != 200:
        print('query failed')

    data = data['daily']
    return data
