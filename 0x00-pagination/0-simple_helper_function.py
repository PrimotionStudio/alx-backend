#!/usr/bin/env python3
"""
This module contains the function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of size
    two containing a start index and an end index
    """
    return ((page * page_size) - page_size, page * page_size)
