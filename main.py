from datetime import datetime

import requests
from typing import Collection

from extensions import _add_stop

from mitmproxy.http import HTTPFlow


endpoint = 'https://api.tomtom.com/search/2/geocode/{}.json'

parameters = {
    'key': 'xbOQYdu7BJG9tEZhFrPnPQq4En9FHv6D'
}


def request(flow: HTTPFlow):
    _add_stop(flow, 53.4497072, -2.261636)

def _geocode_address(address: str) -> Collection[float]:
    print(f'[?] Querying address: {endpoint.format(address)}')
    result = requests.get(
        endpoint.format(address), params=parameters
    ).json()['results'][0]['position']
    print(f'[!] Found location: {result}')
    return result['lat'], result['lon']


def _nearest_crime(longitude: float, latitude: float) -> str:
    print(f'[?] Querying crimes: {longitude, latitude}')
    current_date = datetime.now().strftime('%Y-%m')
    print(current_date)
    results = requests.get(
        'https://data.police.uk/api/crimes-at-location',
        params={'lat': latitude, 'lng': longitude, 'date': current_date}
    )
    return results.text


def _crime_from_address(address: str) -> str:
    return _nearest_crime(*_geocode_address(address))

