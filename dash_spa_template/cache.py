from flask_caching import Cache


CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'simple',  # 'redis',
    # 'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'localhost:6379')
}
_cache = None


def get_cache():
    # type: () -> Cache
    return _cache


def init_cache(app):
    """
    Initializes the cache data structures.

    Args:
        app:

    Returns:
        None
    """
    global _cache
    _cache = Cache()
    _cache.init_app(app.server, config=CACHE_CONFIG)


def add_to_cache(cache_key, value, update=False):
    # type: (str, dict, bool) -> None
    """
    Adds cache_key: value to the cache, or merges value into existing cached value.

    Args:
        cache_key (str): cache key to update.
        value (dict) value to store in cache.
        update (bool): Set to True to merge 'value' into existing cached value.

    Returns:
        None
    """
    if update:
        d = get_from_cache(cache_key)
        d.update(value)
        _cache.set(cache_key, d)
    else:
        _cache.set(cache_key, value)


def get_from_cache(cache_key, default={}):
    # type: (str, dict) -> dict
    """
    Returns the cached value for the cache_key. If the cache_key doesn't exist, returns default.

    Args:
        cache_key (str): cache key to get.
        default (dict): Default value if cache key doesn't exist. Defaults to {}.

    Returns:
        A dict: the cached value.
    """
    d = _cache.get(cache_key)
    return d if d is not None else default


def get_subkey_from_cache(cache_key, sub_key, default=None):
    """
    Retrieves the dict at cache_key location, and then returns a value of the retrieved dict.

    Args:
        cache_key (str): cache key to get
        sub_key (str): cached dict value key to return
        default: default value if sub_key doesn't exist in cached value.

    Returns:
        A value from the cached dict value, or default.
    """
    return get_from_cache(cache_key).get(sub_key, default)


def add_or_get_from_cache(cache_key, sub_key, value, update=False):
    """
    Adds the sub_key's value if value is not None, or otherwise gets the value from the cache.

    Args:
        cache_key (str): cache key to add or update
        sub_key (str): cached dict value key to return
        value: value to store in the cached value dict's sub_key
        update (bool): Set to True to update the cache if cache_key exists.

    Returns:
        Returns the value
    """
    if value is not None:
        add_to_cache(cache_key, {sub_key: value}, update)
    else:
        value = get_subkey_from_cache(cache_key, sub_key)
    return value


# Helper functions to manage cache of layout values


def register_layout(key, value):
    add_to_cache(key, value)


def get_layout_values(key):
    layout_cache = get_from_cache(key)
    return layout_cache


def update_layout_values(key, value):
    add_to_cache(key, value, True)
