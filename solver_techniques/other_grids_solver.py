from get_grid_number import get_grid_number
from column_or_row_numbers_to_check_within_the_grid import column_or_row_numbers_to_check_within_the_grid
from get_adjacent_grids import get_first_vertical_adjacent_grid,get_second_vertical_adjacent_grid,get_first_horizontal_adjacent_grid,get_second_horizontal_adjacent_grid
from get_grid import get_grid
from is_candidate_unique_in_its_column import is_candidate_unique_in_its_column
from is_candidate_in_both_other_column import is_candidate_in_both_other_column
from is_cell_valid import is_cell_valid
from is_candidate_unique_in_its_row import is_candidate_unique_in_its_row
from is_candidate_in_both_other_row import is_candidate_in_both_other_row

def other_grids_solver(candidates_board,board_template):
    # starting with columns
    for row in range(0, 9):
        for column in range(0, 9):
            cell_candidates = candidates_board[row][column]
            if len(cell_candidates) > 0:
                for candidate in cell_candidates:
                    grid_number = get_grid_number(row, column)
                    # columns check
                    columns_to_check = (
                        column_or_row_numbers_to_check_within_the_grid(column)
                    )
                    first_vertical_adjacent_grid_number = (
                        get_first_vertical_adjacent_grid(grid_number)
                    )
                    first_grid_candidates = get_grid(
                        candidates_board, first_vertical_adjacent_grid_number
                    )
                    second_vertical_adjacent_grid_number = (
                        get_second_vertical_adjacent_grid(grid_number)
                    )
                    second_grid_candidates = get_grid(
                        candidates_board, second_vertical_adjacent_grid_number
                    )
                    # 1: check if the candidate is alone in its column
                    is_candidate_unique = is_candidate_unique_in_its_column(
                        candidates_board, candidate, column
                    )
                    # 2: if true, check if at least same candidate in other columns of vertical grids
                    is_candidate_in_both_other_grids_columns = (
                        is_candidate_in_both_other_column(
                            first_grid_candidates, columns_to_check, candidate
                        )
                        and is_candidate_in_both_other_column(
                            second_grid_candidates, columns_to_check, candidate
                        )
                    )

                    should_fill_candidate = (
                        is_candidate_unique
                        and is_candidate_in_both_other_grids_columns
                    )
                    if should_fill_candidate == True:
                        is_cell_valid(board_template, row, column, candidate)
                        board_template[row][column] = candidate
                        recall()

                    # rows check
                    rows_to_check = column_or_row_numbers_to_check_within_the_grid(
                        row
                    )
                    first_horizontal_adjacent_grid_number = (
                        get_first_horizontal_adjacent_grid(grid_number)
                    )
                    first_grid_candidates = get_grid(
                        candidates_board, first_horizontal_adjacent_grid_number
                    )
                    second_horizontal_adjacent_grid_number = (
                        get_second_horizontal_adjacent_grid(grid_number)
                    )
                    second_grid_candidates = get_grid(
                        candidates_board, second_horizontal_adjacent_grid_number
                    )
                    # 1: check if the candidate is alone in its row
                    is_candidate_unique = is_candidate_unique_in_its_row(
                        candidates_board, candidate, row
                    )
                    # 2: if true, check if at least same candidate in other rows of horizontal grids
                    is_candidate_in_both_other_grids_rows = (
                        is_candidate_in_both_other_row(
                            first_grid_candidates, rows_to_check, candidate
                        )
                        and is_candidate_in_both_other_row(
                            second_grid_candidates, rows_to_check, candidate
                        )
                    )
                    should_fill_candidate = (
                        is_candidate_unique
                        and is_candidate_in_both_other_grids_rows
                    )
                    if should_fill_candidate == True:
                        is_cell_valid(board_template, row, column, candidate)
                        board_template[row][column] = candidate
                        #recall()
