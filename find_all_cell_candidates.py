from find_missing_numbers import find_missing_numbers
from flatten_unique import flatten_unique

def find_all_cell_candidates(board_template, row, column):
    non_empty_cells = []
    # get all non empty cells in the current grid
    grid_row = (row // 3) * 3  # Starting row index of the current grid
    grid_column = (column // 3) * 3  # Starting column index of the current grid
    for i in range(grid_row, grid_row + 3):
        for j in range(grid_column, grid_column + 3):
            non_empty_cells.append(board_template[i][j])

    # get all non empty cells in the current row
    non_empty_cells.append(board_template[row])
    # get all non empty cells in the current column
    for i in range(0,9):
        non_empty_cells.append(board_template[i][column])

    unique_non_empty_cells = flatten_unique(non_empty_cells)
    candidates = find_missing_numbers(unique_non_empty_cells)
    return candidates