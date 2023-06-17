from flatten_list import flatten_list
from find_unique_item import find_unique_item


def is_candidate_unique_in_its_column(board, candidate, column):
    same_candidates_in_other_rows = []
    for sub_row in range(0, 9):
        row_candidates = board[sub_row][column]
        if len(row_candidates) > 1:
            same_candidates_in_other_rows.append(row_candidates)
    flatten_same_candidates_in_other_rows = flatten_list(same_candidates_in_other_rows)
    is_candidate_unique = (
        find_unique_item(flatten_same_candidates_in_other_rows) == candidate
    )
    return is_candidate_unique
