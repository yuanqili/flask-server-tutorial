from pprint import pprint

import requests

if __name__ == '__main__':
    response = requests.get('https://geoapi.qweather.com/v2/city/lookup', params={
        'location': '南京',
        'key': '761cdaa96615403e89973211848655d6',
    })
    if response.status_code != 200:
        print('request failed')
    data = response.json()
    if data['code'] != 200:
        print('query failed')

    location_id = data['location'][0]['id']
    print(f'requested location id: {location_id}')

    response = requests.get('https://devapi.qweather.com/v7/weather/7d', params={
        'location': location_id,
        'key': '761cdaa96615403e89973211848655d6',
    })
    data = response.json()
    if data['code'] != 200:
        print('query failed')

    pprint(data['daily'])

