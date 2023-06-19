from get_grid_number import get_grid_number
from get_grid import get_grid

# add a rule for removing all couples if alone on these cells
# example: 7,3 and 7,3 on two candidates cells => remove them elsewhere in the grid
def remove_candidates_if_formed_couples(candidates_board):
    for row in range(9):
        for column in range(9):
            current_grid_number = get_grid_number(row, column)
            current_grid = get_grid(candidates_board, current_grid_number)
            flatten_grid = [item for sublist in current_grid for item in sublist]
            for candidates in flatten_grid:
                if (len(candidates) == 2 and flatten_grid.count(candidates) > 1):
                    if (candidates_board[row][column] != candidates):
                        for item in candidates:
                            if (item in candidates_board[row][column]):
                                candidates_board[row][column].remove(item)
                                