#!/usr/bin/env python3
"""
This module contains the function
"""
import csv
import math
from typing import Tuple, List, Dict, Optional, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of size
    two containing a start index and an end index
    """
    return ((page * page_size) - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This function returns the appropriate
        page of the dataset
        """
        self.dataset()
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List[List],
                                                          Optional[int]]]:
        """
        This function returns a dictionary
        containing the pagination information
        """
        self.dataset()
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        print(len(self.__dataset))
        pages = math.ceil(len(self.__dataset) / page_size)
        prev_page = page - 1
        next_page = page + 1
        if page <= 1:
            prev_page = None
        if page >= pages:
            next_page = None
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": pages
        }
