def find_occurrences(grid):
    occurrences = {}
    for sublist in grid:
        for num in sublist:
            if num in occurrences:
                occurrences[num].append(sublist)
            else:
                occurrences[num] = [sublist]
    return occurrences

