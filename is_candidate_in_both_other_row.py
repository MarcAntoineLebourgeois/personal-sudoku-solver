def is_candidate_in_both_other_row(grid_to_check, rows_to_check, candidate):
    first_row_candidates = []
    second_row_candidates = []
    for row in rows_to_check:
        for column in range(3):
            if (row == rows_to_check[0] and len(grid_to_check[row][column]) > 0):
                first_row_candidates.extend(grid_to_check[row][column])
            if (row == rows_to_check[1] and len(grid_to_check[row][column]) > 0):
                second_row_candidates.extend(grid_to_check[row][column])
    is_candidate_in_first_row = candidate in first_row_candidates
    is_candidate_in_second_row = candidate in second_row_candidates
    is_candidate_in_both_other_row = is_candidate_in_first_row and is_candidate_in_second_row
    return is_candidate_in_both_other_row