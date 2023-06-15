def is_candidate_in_both_other_column(grid_to_check, columns_to_check, candidate):
    first_column_candidates = []
    second_column_candidates = []
    for column in columns_to_check:
        for row in grid_to_check:
            if (column == columns_to_check[0] and len(row[column]) > 0):
                first_column_candidates.extend(row[column])
            if (column == columns_to_check[1] and len(row[column]) > 0):
                second_column_candidates.extend(row[column])
    is_candidate_in_first_column = candidate in first_column_candidates
    is_candidate_in_second_column = candidate in second_column_candidates
    is_candidate_in_both_other_column = is_candidate_in_first_column and is_candidate_in_second_column
    return is_candidate_in_both_other_column