from print_sudoku import print_sudoku
from find_all_cell_candidates import find_all_cell_candidates

# Exemple of a sudoku grid
board_template = [
    [0, 1, 3, 7, 0, 4, 5, 8, 9],
    [0, 5, 4, 0, 9, 0, 0, 0, 0],
    [0, 8, 2, 1, 5, 6, 0, 7, 3],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 4, 7],
    [3, 0, 0, 0, 0, 1, 2, 5, 0],
    [0, 0, 0, 6, 3, 0, 7, 9, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 3, 0, 2, 0, 7, 0, 0, 0]
]

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


def fill_candidates():
    candidates_board = [
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
    # find all candidates
    for row in range(0,9):
        for column in range(0,9):
            cell = board_template[row][column]
            if cell > 0:
                append_board(candidates_board, [],row,column)
            else:
                candidates = find_all_cell_candidates(board_template,row,column)
                append_board(candidates_board, candidates, row, column)
    #print("candidates_board",print_sudoku(candidates_board))
    return candidates_board




def solver ():
    #print("input",print_sudoku(board_template))

    def fill_one_possibility_board():
        candidates_board = fill_candidates()
        # fill the board if only one possibily in candidates_board
        for row in range(0,9):
            for column in range(0,9):
                candidate = candidates_board[row][column][0]
                if len(candidate) == 1:
                    board_template[row][column] = candidate[0]
                    fill_one_possibility_board()

    fill_one_possibility_board()
    print("output2",print_sudoku(board_template))
    #print("board_template",print_sudoku(board_template))


def append_board(board,candidates, row, column):
    board[row][column].append(candidates)


    


#fill_candidates()
solver()
#append_empty_board_candidates(1,0,0)
#find_all_cell_candidates(0,0)