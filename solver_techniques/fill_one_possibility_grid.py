from flatten_list import flatten_list
from find_unique_item import find_unique_item
from is_cell_valid import is_cell_valid

def fill_one_possibility_grid(candidates_board,board_template,recall):
    # find alone possibility in the grid
    for grid_row in [0, 3, 6]:
        for grid_column in [0, 3, 6]:
            grid_candidates = []
            for i in range(grid_row, grid_row + 3):
                for j in range(grid_column, grid_column + 3):
                    if len(candidates_board[i][j]) > 0:
                        grid_candidates.append(candidates_board[i][j])
            flatten_grid_candidates = flatten_list(grid_candidates)
            unique_item = find_unique_item(flatten_grid_candidates)
            if unique_item != 0:
                # I need to find the position of the 2 in the candidates_board
                def find_unique_item_position():
                    for i in range(grid_row, grid_row + 3):
                        for j in range(grid_column, grid_column + 3):
                            if (
                                len(candidates_board[i][j]) > 0
                                and unique_item in candidates_board[i][j]
                            ):
                                return [i, j]

                [item_row, item_column] = find_unique_item_position()
                is_cell_valid(board_template, item_row, item_column, unique_item)
                board_template[item_row][item_column] = unique_item
                print("unique grid item",unique_item,"found in row",item_row,"column",item_column)
                recall()
