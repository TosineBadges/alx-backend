#!/usr/bin/env python3
“””Hypermedia pagination sample.
“””
Import csv
Import math
From typing import Dict, List, Tuple


Def index_range(page: int, page_size: int) -> Tuple[int, int]:
    “””Retrieves the index range from a given page and page size.
    “””
    Start = (page – 1) * page_size
    End = start + page_size
    Return (start, end)


Class Server:
    “””Server class to paginate a database of popular baby names.
    “””
    DATA_FILE = “Popular_Baby_Names.csv”

    Def __init__(self):
        “””Initializes a new Server instance.
        “””
        Self.__dataset = None

    Def dataset(self) -> List[List]:
        “””Cached dataset
        “””
        If self.__dataset is None:
            With open(self.DATA_FILE) as f:
                Reader = csv.reader(f)
                Dataset = [row for row in reader]
            Self.__dataset = dataset[1:]

        Return self.__dataset

    Def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        “””Retrieves a page of data.
        “””
        Assert type(page) == int and type(page_size) == int
        Assert page > 0 and page_size > 0
        Start, end = index_range(page, page_size)
        Data = self.dataset()
        If start > len(data):
            Return []
        Return data[start:end]

    Def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        “””Retrieves information about a page.
        “””
        Page_data = self.get_page(page, page_size)
        Start, end = index_range(page, page_size)
        Total_pages = math.ceil(len(self.__dataset) / page_size)
        Page_info = {
            ‘page_size’: len(page_data),
            ‘page’: page,
            ‘data’: page_data,
            ‘next_page’: page + 1 if end < len(self.__dataset) else None,
            ‘prev_page’: page – 1 if start > 0 else None,
            ‘total_pages’: total_pages,
        }
        Return page_info
