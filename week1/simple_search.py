def search_for(item, list_to_search_in):
    for x in list_to_search_in:
        if x == item:
            return True
    return False