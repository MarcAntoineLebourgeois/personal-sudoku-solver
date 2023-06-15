from print_sudoku import print_sudoku
from find_all_cell_candidates import find_all_cell_candidates
from flatten_list import flatten_list
from find_unique_item import find_unique_item
from get_grid_number import get_grid_number
from get_adjacent_grids import get_first_vertical_adjacent_grid, get_second_vertical_adjacent_grid
from get_grid import get_grid
from column_numbers_to_check_within_the_grid import column_numbers_to_check_within_the_grid
from is_candidate_unique_in_its_column import is_candidate_unique_in_its_column
from is_candidate_in_both_other_column import is_candidate_in_both_other_column

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Exemple of a sudoku grid
board_template = [
    [0, 0, 0, 0, 6, 0, 0, 0, 4],
    [0, 0, 0, 4, 2, 9, 0, 8, 5],
    [0, 1, 0, 3, 0, 8, 0, 0, 2],
    [0, 7, 0, 0, 8, 4, 0, 3, 1],
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [5, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 7, 0, 3, 0, 0, 0, 6],
    [0, 9, 0, 7, 0, 5, 2, 0, 0],
    [0, 0, 0, 1, 0, 6, 0, 0, 3]
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
        for row in range(0,9):
            for column in range(0,9):
                cell_candidates = candidates_board[row][column]
                if len(cell_candidates) == 1:
                    # fill the board if only one possibily in candidates_board
                    board_template[row][column] = cell_candidates[0]
                    fill_one_possibility_board()
    
    fill_one_possibility_board()

    def fill_one_possibility_grid():
        #find alone possibility in the grid
        for grid_row in [0,3,6]:
            for grid_column in [0,3,6]:
                candidates_board = fill_candidates()
                grid_candidates = []
                for i in range(grid_row, grid_row + 3):
                    for j in range(grid_column, grid_column + 3):
                        if len(candidates_board[i][j]) > 0:
                            grid_candidates.append(candidates_board[i][j])
                flatten_grid_candidates = flatten_list(grid_candidates)
                unique_item = find_unique_item(flatten_grid_candidates)
                if (unique_item != 0):


                    # I need to find the position of the 2 in the candidates_board
                    def find_unique_item_position():
                        for i in range(grid_row, grid_row + 3):
                            for j in range(grid_column, grid_column + 3):
                                if (len(candidates_board[i][j]) > 0 and unique_item in candidates_board[i][j]):
                                    return [i,j]


                    [item_row, item_column] = find_unique_item_position()
                    board_template[item_row][item_column] = unique_item
                    fill_one_possibility_grid()
                    continue
            
    fill_one_possibility_grid()
    
    # now, what I need to do is to eliminate candidates based on the other grids
    # such as, if col1 and col3 have the same number in grid 4 and 7
    # then the number in obviously in column 2 in grid 1
    # we will call this technique, other_grids_solver





    def other_grids_solver():
        candidates_board = fill_candidates()
        print("candidates_board",print_sudoku(candidates_board))
        #print("candidates_board",candidates_board)
        #starting with columns
        for row in range(0,9):
            for column in range(0,9):
                cell_candidates = candidates_board[row][column]
                if len(cell_candidates) > 0:
                    #1: check if the candidate is alone in its column
                    for candidate in cell_candidates:
                        if (candidate == 6 and column == 1):
                            columns_to_check = column_numbers_to_check_within_the_grid(column)
                            grid_number = get_grid_number(row, column)
                            first_vertical_adjacent_grid_number = get_first_vertical_adjacent_grid(grid_number)
                            first_grid_candidates = get_grid(candidates_board,first_vertical_adjacent_grid_number)
                            second_vertical_adjacent_grid_number = get_second_vertical_adjacent_grid(grid_number)
                            second_grid_candidates = get_grid(candidates_board,second_vertical_adjacent_grid_number)

                            #2: if true, check if at least same candidate in other columns of vertical grids
                            is_candidate_unique = is_candidate_unique_in_its_column(candidates_board, candidate, column)
                            is_candidate_in_both_other_grids_columns = is_candidate_in_both_other_column(first_grid_candidates,columns_to_check, candidate) and is_candidate_in_both_other_column(second_grid_candidates,columns_to_check, candidate)
                            
                            should_fill_candidate = is_candidate_unique and is_candidate_in_both_other_grids_columns
                            if (should_fill_candidate == True):
                                board_template[row][column] = candidate

    other_grids_solver()
    #print("candidates_board",print_sudoku(candidates_board))


    print("output",print_sudoku(board_template))
    #print("board_template",print_sudoku(board_template))


def append_board(board,candidates, row, column):
    board[row][column] = candidates


    


#fill_candidates()
solver()
#get_specific_grid_candidates(1)

#append_empty_board_candidates(1,0,0)
#find_all_cell_candidates(0,0)