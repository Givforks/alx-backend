#!/usr/bin/env python3
"""Pagination assistant function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Get the index range from a given page and page size
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
