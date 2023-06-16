def print_sudoku(board):
    for i in range(9):
        # Print horizontal lines after every third row
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            # Print vertical lines after every third column
            if j % 3 == 0 and j != 0:
                print("...", end=" ")
            
            # Print the cell value or a placeholder for an empty cell
            if board[i][j] == 0:
                print("_", end=" ")
            else:
                print(board[i][j], end=" ")
        
        print()

