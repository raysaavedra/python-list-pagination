# python-list-pagination
Pagination for list in python

#How to use
from .pagination import get_paginated_list

page = 1
limit = 10
list = []

pagination = get_paginated_list(list, page, limit)