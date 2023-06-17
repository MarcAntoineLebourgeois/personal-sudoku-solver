def get_board_column_from_column_index(board, column_index):
    column = []
    for row in range(9):
        column.append(board[row][column_index])
    return column
