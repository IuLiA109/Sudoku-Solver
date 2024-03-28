def isValidSudoku(board, givenRow, givenColumn, number):
    aux = board[givenRow][givenColumn]
    board[givenRow][givenColumn] = number
    for row in range(9):
        for column in range(9):
            if board[row][column] != 0:
                # check if the element is unique on the column
                for r in range(row+1, 9):
                    if board[row][column] == board[r][column]:
                        board[givenRow][givenColumn] = aux
                        return False
                # check if the element is unique on the row
                for c in range(column+1, 9):
                    if board[row][column] == board[row][c]:
                        board[givenRow][givenColumn] = aux
                        return False
                # check if the element is unique in its 3*3 square
                # check secondary diagonal
                if board[row][column] == board[(row+1) % 3 + 3*(row//3)][(column+1) % 3 + 3*(column//3)]:
                    board[givenRow][givenColumn] = aux
                    return False
                if board[row][column] == board[(row+2) % 3 + 3*(row//3)][(column+2) % 3 + 3*(column//3)]:
                    board[givenRow][givenColumn] = aux
                    return False

                # main diagonal
                if board[row][column] == board[(row+2) % 3 + 3*(row//3)][(column+1) % 3 + 3*(column//3)]:
                    board[givenRow][givenColumn] = aux
                    return False
                if board[row][column] == board[(row+1) % 3 + 3*(row//3)][(column+2) % 3 + 3*(column//3)]:
                    board[givenRow][givenColumn] = aux
                    return False
    board[givenRow][givenColumn] = aux
    return True

def solveSudoku(board, row, column):
    # if the value of the column is 9 we should go to the next row and first column
    if column == 9:
        if row == 8: # if we are at the last row and complete it all it means we finished the game
            return True
        row += 1
        column = 0

    # if the cell is not empty move to the next cell
    if board[row][column] > 0:
        return solveSudoku(board, row, column+1)

    for value in range(1, 10):
        if isValidSudoku(board,row,column,value):
            board[row][column] = value
            # check for next cell
            if solveSudoku(board, row, column+1):
                return True
            # if it reaches here it means that the value was wrong, back to empty cell
            board[row][column] = 0
    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(solveSudoku(grid,0,0))
for row in grid:
    print(row)