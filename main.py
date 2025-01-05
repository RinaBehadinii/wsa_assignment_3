from api_client.cache import fetch_cached_data
from api_client.fetch import fetch_data_with_rate_limit
from api_client.retry import fetch_data_with_backoff
from api_client.validation import validate_api_response

if __name__ == "__main__":
    print("Fetching with rate limit:")
    fetch_data_with_rate_limit()

    print("\nFetching with retry and backoff:")
    fetch_data_with_backoff()

    print("\nFetching with caching:")
    print(fetch_cached_data())  # First call: from API
    print(fetch_cached_data())  # Second call: from cache

    print("\nTesting API validation:")
    if validate_api_response():
        print("Validation test passed.")
    else:
        print("Validation test failed.")
