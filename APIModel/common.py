import requests


def http_request_get(url):
    headers = {
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/54.0.2840.99 Safari/537.36",
    }
    with requests.get(url, headers=headers, stream=False) as response:
        response.encoding = 'utf-8'
        return response
