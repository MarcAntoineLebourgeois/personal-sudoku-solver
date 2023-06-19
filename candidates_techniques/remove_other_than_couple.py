from get_grid_number import get_grid_number
from get_grid import get_grid
from find_occurrences import find_occurrences
from itertools import combinations

def remove_other_than_couple(candidates_board):
    for row in range(9):
        for column in range(9):
            current_grid_number = get_grid_number(row, column)
            current_cell = candidates_board[row][column]
            if len(current_cell) > 0:
                current_grid = get_grid(candidates_board, current_grid_number)
                flatten_grid = [item for sublist in current_grid for item in sublist]
                occurrences = find_occurrences(flatten_grid)
                pairs = []
                for figure in occurrences:
                    if len(occurrences[figure]) == 2:
                        pairs.append(figure)

                def generate_pairs(figures):
                    pairs = [list(pair) for pair in combinations(figures, 2)]
                    return pairs
                def count_pair_occurrences(grid, pairs):
                    occurrences = {}
                    for pair in pairs:
                        count = 0
                        for sublist in grid:
                            if all(num in sublist for num in pair):
                                count += 1
                        occurrences[tuple(pair)] = count
                    return occurrences
                pairs = generate_pairs(pairs)
                pairs_counter = count_pair_occurrences(flatten_grid,pairs)
                current_cell = candidates_board[row][column]
                for pair, count in pairs_counter.items():
                    if count == 2 and pair[0] in current_cell and pair[1] in current_cell:
                        candidates_board[row][column] = list(pair)
                        #recall()

