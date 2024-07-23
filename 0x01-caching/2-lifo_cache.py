#!/usr/bin/env python3
"""
This module contains the function
"""
BaseCaching = __import__('base_cachng').BaseCaching


class LIFOCache(BaseCaching):
    """
    This class inherits from BaseCaching and
    uses the methods of the parent class
    """
    def __init__(self):
        """
        This method initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        This method put an item in the cache
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        This method gets an item from the cache
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
