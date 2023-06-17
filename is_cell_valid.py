from get_board_row_from_cell import get_board_row_from_cell
from get_board_column_from_column_index import get_board_column_from_column_index
from get_grid_number import get_grid_number
from get_grid import get_grid


def is_cell_valid(board, row, column, candidate):
    # do nothing if cell already fill
    if board[row][column] != 0:
        return True
    # check on column
    column_to_check = get_board_column_from_column_index(board, column)
    if candidate in column_to_check:
        raise ValueError(
            candidate,
            "candidate already belong to column",
            column_to_check,
            "at position",
            row,
            column,
        )
    # check on row
    row_to_check = get_board_row_from_cell(board, row)
    if candidate in row_to_check:
        raise ValueError(
            candidate,
            "candidate already belong to row",
            row_to_check,
            "at position",
            row,
            column,
        )
    # check on grid
    grid_number = get_grid_number(row, column)
    grid = get_grid(board, grid_number)
    for cell in grid:
        if candidate in cell:
            raise ValueError(
                candidate,
                "candidate already belong to grid",
                grid,
                "at position",
                row,
                column,
            )
    return True
