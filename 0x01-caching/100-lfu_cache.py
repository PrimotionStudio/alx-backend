#!/usr/bin/env python3
"""
This module contains the function
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    This class inherit from BaseCaching and
    uses the methods of the parent class
    """
    def __init__(self):
        """
        This method initializes the class
        """
        super().__init__()
        # 0 is MRU, -1 is LRU
        self.count = {}

    def put(self, key, item):
        """
        This method puts an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.count[key] += 1
            self.cache_data[key] = item
            return
        if key not in self.cache_data.keys() \
            and len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.count[key] = 1
            self.cache_data[key] = item
            return
        if key not in self.cache_data.keys() \
            and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the LFU
            print(f"DISCARD: {self.get_lfu()}")
            popped = self.cache_data.pop(self.get_lfu())
            self.count.pop(self.get_lfu())
            # print("Just POPPED OUT:", popped)
        self.count[key] = 1
        self.cache_data[key] = item
        # print("Cache is of lenght:", len(self.cache_data))
        # print("MAX ITEMS:", BaseCaching.MAX_ITEMS)

    def get(self, key):
        """
        This method gets an item from the cache
        """
        # print("GET:", key)
        if key is not None and key in self.cache_data.keys():
            self.count[key] += 1
            return self.cache_data[key]
        else:
            return None

    def get_lfu(self):
        """
        This method returns the LFU
        """
        # Initialize variables to track the smallest value and its corresponding key
        min_key = None
        min_value = float('inf')
        # Iterate through the dictionary
        for key, value in self.count.items():
            if value < min_value:
                min_value = value
                min_key = key
        
        return min_key