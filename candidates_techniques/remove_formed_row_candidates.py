from get_grid_number import get_grid_number
from get_grid import get_grid
from flatten_unique import flatten_unique
from get_grid_rows_index_by_row import get_grid_rows_index_by_row

def remove_formed_row_candidates(candidates_board):
    for row in range(0, 9):
        for column in range(0, 9):
            current_grid_number = get_grid_number(row, column)
            current_grid = get_grid(candidates_board, current_grid_number)
            candidates = candidates_board[row][column]

            # IMPORTANT: osef du numéro de la colonne vu qu'on parse chaque candidate
            def get_row_formed_by_candidate(candidate):
                row1_candidates = flatten_unique(
                    [current_grid[0][0], current_grid[0][1], current_grid[0][2]]
                )
                row2_candidates = flatten_unique(
                    [current_grid[1][0], current_grid[1][1], current_grid[1][2]]
                )
                row3_candidates = flatten_unique(
                    [current_grid[2][0], current_grid[2][1], current_grid[2][2]]
                )
                if (
                    candidate in row1_candidates
                    and candidate not in row2_candidates
                    and candidate not in row3_candidates
                ):
                    return 1
                elif (
                    candidate not in row1_candidates
                    and candidate in row2_candidates
                    and candidate not in row3_candidates
                ):
                    return 2
                elif (
                    candidate not in row1_candidates
                    and candidate not in row2_candidates
                    and candidate in row3_candidates
                ):
                    return 3
                else:
                    return None

            for candidate in candidates:
                formed_row = get_row_formed_by_candidate(candidate)
                if formed_row != None:
                    all_columns = list(range(9))
                    columns_to_remove = get_grid_rows_index_by_row(column)
                    columns_to_parse = [
                        x for x in all_columns if x not in columns_to_remove
                    ]
                    for candidates_board_column in columns_to_parse:
                        if (
                            candidate
                            in candidates_board[row][candidates_board_column]
                        ):
                            candidates_board[row][candidates_board_column].remove(
                                candidate
                            )
                            print(candidate,"removed from row",row, "column",candidates_board_column)

                            #recall()
