
def get_paginated_list(items, page, limit):
    '''
        Custom pagination for any list.
        items = array/list
        page = current page number
        limit = number of items to be shown on page
    '''
    obj = {}

    count = len(items)

    obj['limit'] = limit

    if count <= limit:
        total_pages = 1
        limit = count
    else:
        total_pages = count / limit;

    start = (page - 1) * limit
    end = start + limit

    if end > count:
        end = count
    
    if page > total_pages or page <= 0:
        return #handle 404 error page

    obj['current_page'] = page
    obj['total_item_count'] = count
    obj['total_pages'] = total_pages

    if page == 1:
        obj['previous'] = ''
        obj['has_previous'] = False
    else:
        obj['previous'] = page - 1
        obj['has_previous'] = True

    if page >= total_pages:
        obj['next'] = ''
        obj['has_next'] = False
    else:
        obj['next'] = page + 1
        obj['has_next'] = True

    obj['items'] = items[start:end]
    return obj
