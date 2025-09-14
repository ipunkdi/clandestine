"""TOR proxy request utility."""

import requests


def tor_request(url: str, timeout: int = 10) -> requests.Response:
    """
    Perform HTTP GET request through TOR proxy.

    Args:
        url (str): Target URL.
        timeout (int): Request timeout in seconds.

    Returns:
        requests.Response: HTTP response object.
    """
    proxies = {
        "http": "socks5://localhost:9050",
        "https": "socks5://localhost:9050",
    }
    return requests.get(url, proxies=proxies, timeout=timeout)
