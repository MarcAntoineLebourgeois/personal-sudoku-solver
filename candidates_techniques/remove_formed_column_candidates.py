from get_grid_number import get_grid_number
from get_grid import get_grid
from flatten_unique import flatten_unique
from get_grid_rows_index_by_row import get_grid_rows_index_by_row
from print_sudoku import print_sudoku

# now, we need another famous technique:
# candidates forming a row or a column can remove other grid possibilities
## it will consist only into complexify the fill_candidates function
def remove_formed_column_candidates(candidates_board):
    print("candidates_board input", print_sudoku(candidates_board))
    for row in range(9):
        for column in range(9):
            current_grid_number = get_grid_number(row, column)
            current_grid = get_grid(candidates_board, current_grid_number)
            candidates = candidates_board[row][column]

            def get_column_formed_by_candidate(candidate):
                column1_candidates = flatten_unique(
                    [current_grid[0][0], current_grid[1][0], current_grid[2][0]]
                )
                column2_candidates = flatten_unique(
                    [current_grid[0][1], current_grid[1][1], current_grid[2][1]]
                )
                column3_candidates = flatten_unique(
                    [current_grid[0][2], current_grid[1][2], current_grid[2][2]]
                )
                if (
                    candidate in column1_candidates
                    and candidate not in column2_candidates
                    and candidate not in column3_candidates
                ):
                    return 1
                elif (
                    candidate not in column1_candidates
                    and candidate in column2_candidates
                    and candidate not in column3_candidates
                ):
                    return 2
                elif (
                    candidate not in column1_candidates
                    and candidate not in column2_candidates
                    and candidate in column3_candidates
                ):
                    return 3
                else:
                    return None

            for candidate in candidates:
                # columns check
                formed_column = get_column_formed_by_candidate(candidate)
                all_rows = list(range(9))
                rows_to_remove = get_grid_rows_index_by_row(row)
                rows_to_parse = [x for x in all_rows if x not in rows_to_remove]
                if formed_column != None:
                    for candidates_board_row in rows_to_parse:
                        if (
                            candidate
                            in candidates_board[candidates_board_row][column]
                        ):
                            candidates_board[candidates_board_row][column].remove(
                                candidate
                            )
                            print(candidate,"removed from row",candidates_board_row, "column",column)
                           #recall()
