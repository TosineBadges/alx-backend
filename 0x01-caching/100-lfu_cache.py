#!/usr/bin/env python3
“””Least Frequently Used caching module.
“””
From collections import OrderedDict

From base_caching import BaseCaching


Class LFUCache(BaseCaching):
    “””Represents an object that allows storing and
    Retrieving items from a dictionary with a LFU
    Removal mechanism when the limit is reached.
    “””
    Def __init__(self):
        “””Initializes the cache.
        “””
        Super().__init__()
        Self.cache_data = OrderedDict()
        Self.keys_freq = []

    Def __reorder_items(self, mru_key):
        “””Reorders the items in this cache based on the most
        Recently used item.
        “””
        Max_positions = []
        Mru_freq = 0
        Mru_pos = 0
        Ins_pos = 0
        For I, key_freq in enumerate(self.keys_freq):
            If key_freq[0] == mru_key:
                Mru_freq = key_freq[1] + 1
                Mru_pos = i
                Break
            Elif len(max_positions) == 0:
                Max_positions.append(i)
            Elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                Max_positions.append(i)
        Max_positions.reverse()
        For pos in max_positions:
            If self.keys_freq[pos][1] > mru_freq:
                Break
            Ins_pos = pos
        Self.keys_freq.pop(mru_pos)
        Self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    Def put(self, key, item):
        “””Adds an item in the cache.
        “””
        If key is None or item is None:
            Return
        If key not in self.cache_data:
            If len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                Lfu_key, _ = self.keys_freq[-1]
                Self.cache_data.pop(lfu_key)
                Self.keys_freq.pop()
                Print(“DISCARD:”, lfu_key)
            Self.cache_data[key] = item
            Ins_index = len(self.keys_freq)
            For I, key_freq in enumerate(self.keys_freq):
                If key_freq[1] == 0:
                    Ins_index = i
                    Break
            Self.keys_freq.insert(ins_index, [key, 0])
        Else:
            Self.cache_data[key] = item
            Self.__reorder_items(key)

    Def get(self, key):
        “””Retrieves an item by key.
        “””
        If key is not None and key in self.cache_data:
            Self.__reorder_items(key)
        Return self.cache_data.get(key, None)
