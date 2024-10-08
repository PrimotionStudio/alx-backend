#!/usr/bin/env python3
"""
This module contains the function
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This class inherits from BaseCaching and
    uses the methods of the parent class
    """

    def put(self, key, item):
        """
        This method puts an item in the cache
        """
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
