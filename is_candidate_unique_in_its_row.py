from flatten_list import flatten_list
from find_unique_item import find_unique_item

def is_candidate_unique_in_its_row(board, candidate, row):
    same_candidates_in_other_columns = []
    for sub_column in range(0,9):
        column_candidates = board[row][sub_column]
        if (len(column_candidates)>1):
            same_candidates_in_other_columns.append(column_candidates)
    flatten_same_candidates_in_other_columns = flatten_list(same_candidates_in_other_columns)
    is_candidate_unique = find_unique_item(flatten_same_candidates_in_other_columns) == candidate
    return is_candidate_unique