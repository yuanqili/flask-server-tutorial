import os
from pprint import pprint

import requests
from flask import render_template, request

from . import app


@app.route('/', methods=['GET'])
def index():
    username = request.args.get('username', 'stranger', type=str)
    show_detail = request.args.get('show_detail', False, type=bool)
    posts = [
        {
            'author': 'Donald Trump',
            'content': 'Make America Great Again!',
        },
        {
            'author': 'Hillary Clinton',
            'content': 'I will be the next president of the United States.',
        },
        {
            'author': 'Bernie Sanders',
            'content': 'I am the only candidate who can beat Donald Trump.',
        },
        {
            'author': 'Ted Cruz',
            'content': 'I am the only candidate who can beat Hillary Clinton.',
        }
    ]
    return render_template('index.html', username=username, show_detail=show_detail, posts=posts)


def get_city_location_id(city):
    response = requests.get('https://geoapi.qweather.com/v2/city/lookup', params={
        'location': city,
        'key': '761cdaa96615403e89973211848655d6',
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
        'key': os.environ['HEFENG_KEY'],
    })
    if response.status_code != 200:
        print('request failed')

    data = response.json()
    if data['code'] != 200:
        print('query failed')

    data = data['daily']
    return data


@app.route('/weather', methods=['GET'])
def query():
    city = request.args.get('city', '南京', type=str)
    data = get_city_7d_weather(city)
    return render_template('weather.html', city=city, data=data)
