import time

import requests

API_URL = "https://hub.culturegraph.org/entityfacts/118540238"


def fetch_data_with_rate_limit():
    requests_made = 0
    RATE_LIMIT = 5

    for _ in range(10):
        if requests_made > 0 and requests_made % RATE_LIMIT == 0:
            print("Rate limit reached. Waiting for 60 seconds...")
            time.sleep(60)
        response = requests.get(API_URL)
        print(f"Request {requests_made + 1}: {response.status_code}")
        requests_made += 1
