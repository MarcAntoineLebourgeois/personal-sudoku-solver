from print_sudoku import print_sudoku
from find_all_cell_candidates import find_all_cell_candidates

from is_sudoku_solved import is_sudoku_solved
from candidates_techniques.remove_formed_column_candidates import remove_formed_column_candidates
from candidates_techniques.remove_formed_row_candidates import remove_formed_row_candidates
from candidates_techniques.remove_candidates_if_formed_couples import remove_candidates_if_formed_couples
from candidates_techniques.remove_other_than_couple import remove_other_than_couple

from solver_techniques.fill_one_possibility_board import fill_one_possibility_board
from solver_techniques.fill_one_possibility_grid import fill_one_possibility_grid
from solver_techniques.other_grids_solver import other_grids_solver

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


# unsolved = board_template = [
#    [0, 9, 0, 0, 0, 0, 2, 0, 0],
#    [0, 0, 0, 0, 0, 5, 0, 8, 0],
#    [0, 0, 8, 4, 0, 0, 0, 1, 0],
#    [0, 0, 6, 0, 0, 1, 3, 0, 5],
#    [0, 5, 0, 0, 0, 9, 7, 0, 6],
#    [4, 0, 0, 2, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 2, 0, 0, 9],
#    [7, 3, 4, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 6, 0, 0, 0, 0]
# ]

# Exemple of a sudoku grid
board_template = [
    [0, 0, 9, 0, 4, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 7, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [5, 1, 0, 0, 0, 0, 0, 0, 3],
    [4, 0, 0, 0, 0, 9, 0, 5, 0],
    [0, 0, 0, 3, 0, 0, 6, 0, 0],
    [0, 0, 0, 5, 1, 4, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 3, 8, 0],
]

empty_board = [
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
]


counter_solver = 0

def fill_candidates():
    candidates_board = [
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
]
    # find all candidates
    for row in range(0, 9):
        for column in range(0, 9):
            cell = board_template[row][column]
            if cell == 0:
                candidates = find_all_cell_candidates(board_template, row, column)
                candidates_board[row][column] = candidates

    
    remove_formed_column_candidates(candidates_board)
    #remove_formed_row_candidates(candidates_board)
    #remove_candidates_if_formed_couples(candidates_board)
    #remove_other_than_couple(candidates_board)
    return candidates_board


def solver():
    candidates_board = fill_candidates()

    fill_one_possibility_board()
    fill_one_possibility_grid()
    other_grids_solver()
    
    is_solved = is_sudoku_solved(board_template)
    if is_solved == False:
        print("sudoku unsolved")


    print("candidates_board", print_sudoku(candidates_board))
    print("output", print_sudoku(board_template))


def append_board(board, candidates, row, column):
    board[row][column] = candidates


#solver()

def solver2():
    candidates_board = fill_candidates()

    print("input", print_sudoku(board_template))

    def update_candidates_board():
        remove_formed_column_candidates(candidates_board)
        remove_formed_row_candidates(candidates_board)
        remove_candidates_if_formed_couples(candidates_board)
        remove_other_than_couple(candidates_board)
        
    #update_candidates_board()

    def update_board():
        
        fill_one_possibility_board(candidates_board, board_template)
        fill_one_possibility_grid(candidates_board, board_template,solver2)

        #other_grids_solver(candidates_board, board_template)

    update_board()
    print("candidates_board", print_sudoku(candidates_board))
    print("output", print_sudoku(board_template))



solver2()




