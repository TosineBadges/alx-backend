#!/usr/bin/env python3
“””Most Recently Used caching module.
“””
From collections import OrderedDict

From base_caching import BaseCaching


Class MRUCache(BaseCaching):
    “””Represents an object that allows storing and
    Retrieving items from a dictionary with an MRU
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
                Mru_key, _ = self.cache_data.popitem(False)
                Print(“DISCARD:”, mru_key)
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
