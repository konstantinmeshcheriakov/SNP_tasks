import time
from functools import wraps
from collections import OrderedDict

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))

            if key in cache:
                result, timestamp = cache[key]
                if seconds is None or time.time() - timestamp < seconds:
                    return result
                else:
                    del cache[key]

            result = func(*args, **kwargs)
            cache[key] = (result, time.time())

            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)

            return result

        return wrapper
    return decorator

