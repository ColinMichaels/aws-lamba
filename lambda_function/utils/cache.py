import os
import pickle

CACHE_DIR = "/tmp"  # Suitable for AWS Lambda as /tmp is the writable directory

def generate_cache_key(function_name, *args, **kwargs):
    """
    Generate a unique cache key based on function name, arguments, and keyword arguments.
    """
    key = f"{function_name}_{'_'.join(map(str, args))}_{'_'.join([f'{k}_{v}' for k, v in kwargs.items()])}"
    return key.replace(' ', '_')  # Ensure no spaces

def cache_results(query, results):
    """
    Decorator to cache the results of a function.
    """
    def wrapper(*args, **kwargs):
        cache_key = generate_cache_key(func.__name__, *args, **kwargs)
        cache_file_path = os.path.join(CACHE_DIR, cache_key)

        # If cache file exists, return its contents
        if os.path.exists(cache_file_path):
            with open(cache_file_path, 'rb') as cache_file:
                return pickle.load(cache_file)

        # Else compute the result, store it in cache, and return
        result = func(*args, **kwargs)
        with open(cache_file_path, 'wb') as cache_file:
            pickle.dump(result, cache_file)

        return result

    return wrapper

def fetch_from_cache(function_name, *args, **kwargs):
    """
    Fetch the result from cache for a given function and its arguments. If not cached, returns None.
    """
    cache_key = generate_cache_key(function_name, *args, **kwargs)
    cache_file_path = os.path.join(CACHE_DIR, cache_key)
    
    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'rb') as cache_file:
            return pickle.load(cache_file)
    return None