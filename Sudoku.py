import copy

class Sudoku:
    def __init__(self, board):
        self.board = copy.deepcopy(board)
    def isValidSudoku(self, givenRow, givenColumn, number):
        aux = self.board[givenRow][givenColumn]
        self.board[givenRow][givenColumn] = number
        for row in range(9):
            for column in range(9):
                if self.board[row][column] != 0:
                    # check if the element is unique on the column
                    for r in range(row + 1, 9):
                        if self.board[row][column] == self.board[r][column]:
                            self.board[givenRow][givenColumn] = aux
                            return False
                    # check if the element is unique on the row
                    for c in range(column + 1, 9):
                        if self.board[row][column] == self.board[row][c]:
                            self.board[givenRow][givenColumn] = aux
                            return False
                    # check if the element is unique in its 3*3 square
                    # check secondary diagonal
                    if self.board[row][column] == self.board[(row + 1) % 3 + 3 * (row // 3)][
                        (column + 1) % 3 + 3 * (column // 3)]:
                        self.board[givenRow][givenColumn] = aux
                        return False
                    if self.board[row][column] == self.board[(row + 2) % 3 + 3 * (row // 3)][
                        (column + 2) % 3 + 3 * (column // 3)]:
                        self.board[givenRow][givenColumn] = aux
                        return False

                    # main diagonal
                    if self.board[row][column] == self.board[(row + 2) % 3 + 3 * (row // 3)][
                        (column + 1) % 3 + 3 * (column // 3)]:
                        self.board[givenRow][givenColumn] = aux
                        return False
                    if self.board[row][column] == self.board[(row + 1) % 3 + 3 * (row // 3)][
                        (column + 2) % 3 + 3 * (column // 3)]:
                        self.board[givenRow][givenColumn] = aux
                        return False
        self.board[givenRow][givenColumn] = aux
        return True

    def solveSudoku(self, row, column):
        # if the value of the column is 9 we should go to the next row and first column
        if column == 9:
            if row == 8:  # if we are at the last row and complete it all it means we finished the game
                return True
            row += 1
            column = 0

        # if the cell is not empty move to the next cell
        if self.board[row][column] > 0:
            return self.solveSudoku(row, column + 1)

        for value in range(1, 10):
            if self.isValidSudoku(row, column, value):
                self.board[row][column] = value
                # check for next cell
                if self.solveSudoku(row, column + 1):
                    return True
                # if it reaches here it means that the value was wrong, back to empty cell
                self.board[row][column] = 0
        return False

    def solvedSudoku(self):
        self.solveSudoku(0,0)
        return self.board
