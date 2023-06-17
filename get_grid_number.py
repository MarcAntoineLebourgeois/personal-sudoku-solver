def get_grid_number(row, column):
    # if (row < 3 and column < 3):
    #    return 1
    # if (row < 6 and column < 3):
    #    return 4
    # if (row < 9 and column < 3):
    #    return 7
    # if (row < 3 and column < 6):
    #    return 2
    # if (row < 3 and column < 9):
    #    return 3
    # if (row < 6 and column < 6):
    #    return 5
    # if (row < 6 and column < 9):
    #    return 6
    # if (row < 9 and column < 6):
    #    return 8
    # if (row < 9 and column < 9):
    #    return 9
    row_number = row // 3
    column_number = column // 3
    grid_number = row_number * 3 + column_number
    return grid_number + 1
