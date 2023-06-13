from print_sudoku import print_sudoku
from find_all_cell_candidates import find_all_cell_candidates

# Exemple of a sudoku grid
board_template = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# this grid will be used to input potential numbers
empty_board = [
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
]

def solver ():
    # print input board
    # print_sudoku(boardTemplate)
    for row in range(0,9):
        for column in range(0,9):
            cell = board_template[row][column]
            if cell > 0:
                append_empty_board_candidates("na",row,column)
            else:
                candidates = find_all_cell_candidates(board_template,row,column)
                append_empty_board_candidates(candidates, row, column)
    print("empty_board",print_sudoku(empty_board))


def append_empty_board_candidates(candidates, row, column):
    empty_board[row][column].append(candidates)

def find_missing_numbers(input_list):
    all_numbers = set(range(1, 10))
    input_set = set(input_list)
    missing_numbers = sorted(all_numbers - input_set)
    return missing_numbers

    



solver()
#append_empty_board_candidates(1,0,0)
#find_all_cell_candidates(0,0)