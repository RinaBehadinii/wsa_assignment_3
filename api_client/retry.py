import logging
import random
import time

import requests

API_URL = "https://hub.culturegraph.org/entityfacts/118540238"

logging.basicConfig(level=logging.INFO)


def fetch_data_with_backoff():
    retries = 0
    max_retries = 5

    while retries < max_retries:
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            logging.info("Data fetched successfully!")
            return response.json()
        except requests.exceptions.RequestException as e:
            wait_time = min(2 ** retries + random.uniform(0, 1), 30)
            logging.warning(f"Error: {e}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
            retries += 1

    logging.error("Max retries reached. Could not fetch data.")
