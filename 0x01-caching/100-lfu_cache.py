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
        self.order = []

    def put(self, key, item):
        """
        This method puts an item in the cache
        """
        # print("PUT:", key)
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.append_order(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the LRU
            print(f"DISCARD: {self.get_lru()}")
            popped = self.cache_data.pop(self.get_lru())
            # print("Just POPPED OUT:", popped)
        self.append_order(key)
        self.cache_data[key] = item
        # print("Cache is of lenght:", len(self.cache_data))
        # print("MAX ITEMS:", BaseCaching.MAX_ITEMS)

    def get(self, key):
        """
        This method gets an item from the cache
        """
        # print("GET:", key)
        if key is not None and key in self.cache_data.keys():
            self.append_order(key)
            return self.cache_data[key]
        else:
            return None

    def append_order(self, key):
        """
        This method appends the key to the order
        """
        if key in self.order:
            self.order.remove(key)
        else:
            if len(self.order) == BaseCaching.MAX_ITEMS:
                self.order.pop(-1)
        # append the key to the beginning to show MRU
        self.order = [key] + self.order
        # print("New Order:", self.order)

    def get_lru(self):
        """
        This method returns the LRU
        """
        return self.order[-1]
