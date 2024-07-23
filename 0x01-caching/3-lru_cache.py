#!/usr/bin/env python3
"""
This module contains the function
"""
BaseCaching = __import__('base_cachng').BaseCaching


class LRUCache(BaseCaching):
    """
    This class inherits from BaseCaching and
    uses the methods of the parent class
    """
    recency = {}


    @classmethod
    def update_recency(cls, key):
        """
        This method updates the recency list
        """
        # 0 index represents the MRU
        # BaseCaching.MAX_ITEMS - 1 index represents the LRU
        LRUCache.recency = {str(i): "" for i in range(BaseCaching.MAX_ITEMS)}
        # if key in LRUCache.recency:
        #     LRUCache.recency.remove(key)
        # LRUCache.recency.append(key)
        # if len(LRUCache.__recency) > BaseCaching.MAX_ITEMS:
        #     LRUCache.__recency.pop(0)

    def __init__(self):
        """
        This method initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        This method puts an item in the cache
        """
        LRUCache.update_recency(key)
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # find the LRU item and POP it
            first_key = list(self.cache_data.keys())[-1]
            # self.cache_data.pop(LRUCache.__recency[0])
            # print(f"DISCARD: {LRUCache.__recency[0]}")

    def get(self, key):
        """
        This method gets an item from the cache
        """
        LRUCache.update_recency(key)
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
