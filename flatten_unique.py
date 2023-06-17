def flatten_unique(arr):
    flattened = []

    def flatten(arr):
        for item in arr:
            if isinstance(item, list):
                flatten(item)
            else:
                flattened.append(item)

    flatten(arr)
    return list(set(flattened))
