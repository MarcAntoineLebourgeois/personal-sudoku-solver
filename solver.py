from print_sudoku import print_sudoku
from find_all_cell_candidates import find_all_cell_candidates
from flatten_list import flatten_list
from find_unique_item import find_unique_item
from get_grid_number import get_grid_number
from get_adjacent_grids import get_first_vertical_adjacent_grid, get_second_vertical_adjacent_grid, get_first_horizontal_adjacent_grid, get_second_horizontal_adjacent_grid
from get_grid import get_grid
from column_or_row_numbers_to_check_within_the_grid import column_or_row_numbers_to_check_within_the_grid
from is_candidate_unique_in_its_column import is_candidate_unique_in_its_column
from is_candidate_in_both_other_column import is_candidate_in_both_other_column
from flatten_unique import flatten_unique
from get_grid_rows_index_by_row import get_grid_rows_index_by_row
from is_candidate_unique_in_its_row import is_candidate_unique_in_its_row
from is_candidate_in_both_other_row import is_candidate_in_both_other_row

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
    [0, 0, 0, 9, 0, 0, 4, 2, 7],
    [0, 0, 0, 0, 8, 0, 0, 1, 5],
    [7, 9, 0, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 8, 6, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 1, 6, 0, 0, 0, 0],
    [0, 0, 9, 0, 4, 0, 8, 0, 0],
    [1, 0, 0, 7, 2, 0, 0, 4, 9],
    [3, 0, 4, 0, 0, 0, 0, 0, 6]
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
    # now, we need another famous technique:
    # candidates forming a row or a column can remove other grid possibilities
    # it will consist only into complexify the fill_candidates function
    for row in range(0,9):
        for column in range(0,9):
            current_grid_number = get_grid_number(row, column)
            current_grid = get_grid(candidates_board, current_grid_number)
            candidates = candidates_board[row][column]


            # IMPORTANT: osef du numéro de la colonne vu qu'on parse chaque candidate
            def get_column_formed_by_candidate(candidate):
                column1_candidates = flatten_unique([current_grid[0][0],current_grid[1][0],current_grid[2][0]])
                column2_candidates = flatten_unique([current_grid[0][1],current_grid[1][1],current_grid[2][1]])
                column3_candidates = flatten_unique([current_grid[0][2],current_grid[1][2],current_grid[2][2]])
                if candidate in column1_candidates and candidate not in column2_candidates and candidate not in column3_candidates:
                    return 1
                elif candidate not in column1_candidates and candidate in column2_candidates and candidate not in column3_candidates:
                    return 2
                elif candidate not in column1_candidates and candidate not in column2_candidates and candidate in column3_candidates:
                    return 3
                else:
                    return None
            def get_row_formed_by_candidate(candidate):
                row1_candidates = flatten_unique([current_grid[0][0],current_grid[0][1],current_grid[0][2]])
                row2_candidates = flatten_unique([current_grid[1][0],current_grid[1][1],current_grid[1][2]])
                row3_candidates = flatten_unique([current_grid[2][0],current_grid[2][1],current_grid[2][2]])
                if candidate in row1_candidates and candidate not in row2_candidates and candidate not in row3_candidates:
                    return 1
                elif candidate not in row1_candidates and candidate in row2_candidates and candidate not in row3_candidates:
                    return 2
                elif candidate not in row1_candidates and candidate not in row2_candidates and candidate in row3_candidates:
                    return 3
                else:
                    return None
                
            for candidate in candidates:
                # columns check
                formed_column = get_column_formed_by_candidate(candidate)
                all_rows = list(range(9))
                rows_to_remove = get_grid_rows_index_by_row(row)
                rows_to_parse = [x for x in all_rows if x not in rows_to_remove]
                if (formed_column != None):
                    for candidates_board_row in rows_to_parse:
                        if candidate in candidates_board[candidates_board_row][column]: 
                            candidates_board[candidates_board_row][column].remove(candidate)
                #rows check 
                formed_row = get_row_formed_by_candidate(candidate)
                all_columns = list(range(9))
                columns_to_remove = get_grid_rows_index_by_row(column)
                columns_to_parse = [x for x in all_columns if x not in columns_to_remove]
                if (formed_row != None):
                    for candidates_board_column in columns_to_parse:
                        if candidate in candidates_board[row][candidates_board_column]: 
                            candidates_board[row][candidates_board_column].remove(candidate)
    return candidates_board



def solver():
    #print("input",print_sudoku(board_template))

    def fill_one_possibility_board():
        candidates_board = fill_candidates()
        for row in range(0,9):
            for column in range(0,9):
                cell_candidates = candidates_board[row][column]
                if len(cell_candidates) == 1:
                    # fill the board if only one possibily in candidates_board
                    board_template[row][column] = cell_candidates[0]
                    solver()
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
                    solver()
                    continue
    fill_one_possibility_grid()
    
    # now, what I need to do is to eliminate candidates based on the other grids
    # such as, if col1 and col3 have the same number in grid 4 and 7
    # then the number in obviously in column 2 in grid 1
    # we will call this technique, other_grids_solver
    def other_grids_solver():
        candidates_board = fill_candidates()
        #print("candidates_board",print_sudoku(candidates_board))
        #print("candidates_board",candidates_board)
        #starting with columns
        for row in range(0,9):
            for column in range(0,9):
                cell_candidates = candidates_board[row][column]
                if len(cell_candidates) > 0:
                    for candidate in cell_candidates:
                        grid_number = get_grid_number(row, column)
                        #columns check
                        columns_to_check = column_or_row_numbers_to_check_within_the_grid(column)
                        first_vertical_adjacent_grid_number = get_first_vertical_adjacent_grid(grid_number)
                        first_grid_candidates = get_grid(candidates_board,first_vertical_adjacent_grid_number)
                        second_vertical_adjacent_grid_number = get_second_vertical_adjacent_grid(grid_number)
                        second_grid_candidates = get_grid(candidates_board,second_vertical_adjacent_grid_number)
                        #1: check if the candidate is alone in its column
                        is_candidate_unique = is_candidate_unique_in_its_column(candidates_board, candidate, column)
                        #2: if true, check if at least same candidate in other columns of vertical grids
                        is_candidate_in_both_other_grids_columns = is_candidate_in_both_other_column(first_grid_candidates,columns_to_check, candidate) and is_candidate_in_both_other_column(second_grid_candidates,columns_to_check, candidate)
                        
                        should_fill_candidate = is_candidate_unique and is_candidate_in_both_other_grids_columns
                        if (should_fill_candidate == True):
                            board_template[row][column] = candidate
                            solver()

                        if (row == 4 and column == 4 and candidate == 7):
                            #rows check
                            rows_to_check = column_or_row_numbers_to_check_within_the_grid(row)
                            first_horizontal_adjacent_grid_number = get_first_horizontal_adjacent_grid(grid_number)
                            first_grid_candidates = get_grid(candidates_board,first_horizontal_adjacent_grid_number)
                            second_horizontal_adjacent_grid_number = get_second_horizontal_adjacent_grid(grid_number)
                            second_grid_candidates = get_grid(candidates_board,second_horizontal_adjacent_grid_number)
                            #1: check if the candidate is alone in its row
                            is_candidate_unique = is_candidate_unique_in_its_row(candidates_board, candidate, row)
                            #2: if true, check if at least same candidate in other rows of horizontal grids
                            is_candidate_in_both_other_grids_rows = is_candidate_in_both_other_row(first_grid_candidates,rows_to_check, candidate) and is_candidate_in_both_other_row(second_grid_candidates,rows_to_check, candidate)
                            should_fill_candidate = is_candidate_unique and is_candidate_in_both_other_grids_rows
                            if (should_fill_candidate == True):
                                board_template[row][column] = candidate
                                solver()
    other_grids_solver()
    

    candidates_board = fill_candidates()
    print("candidates_board",print_sudoku(candidates_board))

    print("output",print_sudoku(board_template))
    #print("board_template",print_sudoku(board_template))


def append_board(board,candidates, row, column):
    board[row][column] = candidates


    


#fill_candidates()
solver()
#get_specific_grid_candidates(1)

#append_empty_board_candidates(1,0,0)
#find_all_cell_candidates(0,0)