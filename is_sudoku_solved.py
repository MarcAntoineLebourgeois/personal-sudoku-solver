def is_sudoku_solved(sudoku):
    for row in sudoku:
        for num in row:
            if num == 0:
                return False
    return True