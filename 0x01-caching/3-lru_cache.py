#!/usr/bin/env python3
“””Least Recently Used caching module.
“””
From collections import OrderedDict

From base_caching import BaseCaching


Class LRUCache(BaseCaching):
    “””Represents an object that allows storing and
    Retrieving items from a dictionary with a LRU
    Removal mechanism when the limit is reached.
    “””
    Def __init__(self):
        “””Initializes the cache.
        “””
        Super().__init__()
        Self.cache_data = OrderedDict()

    Def put(self, key, item):
        “””Adds an item in the cache.
        “””
        If key is None or item is None:
            Return
        If key not in self.cache_data:
            If len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                Lru_key, _ = self.cache_data.popitem(True)
                Print(“DISCARD:”, lru_key)
            Self.cache_data[key] = item
            Self.cache_data.move_to_end(key, last=False)
        Else:
            Self.cache_data[key] = item

    Def get(self, key):
        “””Retrieves an item by key.
        “””
        If key is not None and key in self.cache_data:
            Self.cache_data.move_to_end(key, last=False)
        Return self.cache_data.get(key, None)
