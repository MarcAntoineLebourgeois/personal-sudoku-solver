from is_cell_valid import is_cell_valid

def fill_one_possibility_board(candidates_board,board_template):
    for row in range(0, 9):
        for column in range(0, 9):
            cell_candidates = candidates_board[row][column]
            if len(cell_candidates) == 1:
                # fill the board if only one possibily in candidates_board
                is_cell_valid(board_template, row, column, cell_candidates[0])
                board_template[row][column] = cell_candidates[0]
                print("fill_one_possibility_board:",cell_candidates[0], "found solo in row",row,"column",column)
                #recall()