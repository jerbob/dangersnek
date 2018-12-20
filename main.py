from datetime import datetime
from typing import collection

from mitmproxy.http import HTTPFlow
import requests


endpoint = 'https://api.tomtom.com/search/2/geocode/{}.json'


def _add_stop(flow: HTTPFlow, latitude: float, longitude: float) -> HTTPFlow:
    """Add a stop to the given Google Maps request."""
    url = flow.request.url
    if not url.startswith('https://www.google.com/maps/dir'):
        return
    print(f'[?] Request intercepted: {url}')
    url = url.split('/')
    for i, section in enumerate(url):
        if section.startswith('@'):
            break
    url.insert(i, f"'{latitude},{longitude}'")
    print(
        f'[+] Injected detour with latitude {latitude}, '
        f'longitude {longitude}'
    )
    flow.request.url = '/'.join(url)
    print(f'[?] New request string: {flow.request.url}')


def _geocode_address(address: str) -> Collection[float]:
    """Given an address, return the latitude and longitude values."""
    print(f'[?] Querying address: {endpoint.format(address)}')
    result = requests.get(
        endpoint.format(address), params=parameters
    ).json()['results'][0]['position']
    print(f'[!] Found location: {result}')
    return result['lat'], result['lon']


def _nearest_crime(longitude: float, latitude: float) -> str:
    """Find the nearest crime to a given latitude/longitude point."""
    print(f'[?] Querying crimes: {longitude, latitude}')
    current_date = datetime.now().strftime('%Y-%m')
    print(current_date)
    results = requests.get(
        'https://data.police.uk/api/crimes-at-location',
        params={'lat': latitude, 'lng': longitude, 'date': current_date}
    )
    return results.text


def _crime_from_address(address: str) -> str:
    """Find the nearest crime to a given address."""
    return _nearest_crime(*_geocode_address(address))
