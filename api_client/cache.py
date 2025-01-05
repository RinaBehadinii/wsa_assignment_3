import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=300)
API_URL = "https://hub.culturegraph.org/entityfacts/118540238"


@cached(cache)
def fetch_cached_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
