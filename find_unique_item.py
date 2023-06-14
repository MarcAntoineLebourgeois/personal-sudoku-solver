def find_unique_item(lst):
    for item in lst:
        if lst.count(item) == 1:
            return item
    return 0