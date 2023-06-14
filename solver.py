from print_sudoku import print_sudoku
from find_all_cell_candidates import find_all_cell_candidates
from flatten_list import flatten_list
from find_unique_item import find_unique_item

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
    print("output",print_sudoku(board_template))
    #print("board_template",print_sudoku(board_template))


def append_board(board,candidates, row, column):
    board[row][column] = candidates


    


#fill_candidates()
solver()
#append_empty_board_candidates(1,0,0)
#find_all_cell_candidates(0,0)