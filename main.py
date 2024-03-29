import sys
import pygame
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

class Board:
    def __init__(self, board):
        self.board_width = 9
        self.board_height = 9
        self.cell_size = 50
        self.board = board

        self.cells = []
        for i in range(self.board_height):
            aux = []
            for j in range(self.board_width):
                x = i * self.cell_size
                y = j * self.cell_size
                cell = pygame.Rect(y, x, self.cell_size, self.cell_size)
                aux.append({'cell': cell, 'color': (255, 255, 255)})
            self.cells.append(aux)

    def clickCell(self, row, column):
        x = column
        y = row
        if self.board[y][x] != 0:
            for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                    if y == i or x == j or (y // 3 == i // 3 and x // 3 == j // 3):
                        self.cells[i][j]['color'] = (204, 255, 204)
                    elif self.board[i][j] == self.board[y][x]:
                        self.cells[i][j]['color'] = (153, 255, 204)
                    else:
                        self.cells[i][j]['color'] = (255, 255, 255)
        else:
            for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                    self.cells[i][j]['color'] = (255, 255, 255)
        self.cells[y][x]['color'] = (153, 255, 235)

    def update(self, row, column, value):
        self.board[row][column] = value

class Game:
    def __init__(self, board):
        pygame.init()
        pygame.display.set_caption('SUDOKU')
        self.board = Board(board)
        self.window_width = self.board.board_width * self.board.cell_size
        self.window_height = self.board.board_height * self.board.cell_size + 60
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.key = None
        self.click_column = None
        self.click_row = None
        self.mistake = 0
        self.solvedBoard = Sudoku(board).solvedSudoku()
        self.font = pygame.font.Font('Arial.ttf', 25)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.click_column = x // self.board.cell_size  # width c column
                self.click_row = y // self.board.cell_size  # height l row
                self.board.clickCell(self.click_row, self.click_column)
                print(self.click_row)
                print(self.click_column)
                print(self.board.board[self.click_row][self.click_column])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.key = 1
                if event.key == pygame.K_2:
                    self.key = 2
                if event.key == pygame.K_3:
                    self.key = 3
                if event.key == pygame.K_4:
                    self.key = 4
                if event.key == pygame.K_5:
                    self.key = 5
                if event.key == pygame.K_6:
                    self.key = 6
                if event.key == pygame.K_7:
                    self.key = 7
                if event.key == pygame.K_8:
                    self.key = 8
                if event.key == pygame.K_9:
                    self.key = 9
                if event.key == pygame.K_KP1:
                    self.key = 1
                if event.key == pygame.K_KP2:
                    self.key = 2
                if event.key == pygame.K_KP3:
                    self.key = 3
                if event.key == pygame.K_KP4:
                    self.key = 4
                if event.key == pygame.K_KP5:
                    self.key = 5
                if event.key == pygame.K_KP6:
                    self.key = 6
                if event.key == pygame.K_KP7:
                    self.key = 7
                if event.key == pygame.K_KP8:
                    self.key = 8
                if event.key == pygame.K_KP9:
                    self.key = 9
                if self.solvedBoard[self.click_row][self.click_column] == self.key:
                    if self.board.board[self.click_row][self.click_column] == 0:
                        self.board.update(self.click_row, self.click_column, self.key)
                else:
                    if self.mistake == 2:
                        pygame.quit()
                        sys.exit()
                    if self.board.board[self.click_row][self.click_column] == 0:
                        self.mistake += 1

    def draw_board(self):
        for i in range(self.board.board_height):
            for j in range(self.board.board_width):
                x = i * self.board.cell_size
                y = j * self.board.cell_size
                pygame.draw.rect(self.screen, self.board.cells[i][j]['color'], self.board.cells[i][j]['cell'])
                pygame.draw.rect(self.screen, (0, 0, 0), self.board.cells[i][j]['cell'], 1)
                if self.board.board[i][j] != 0:
                    text_surface = self.font.render(str(self.board.board[i][j]), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center = (y + self.board.cell_size // 2, x + self.board.cell_size // 2))
                    self.screen.blit(text_surface, text_rect)

    def draw_boundary_lines(self):
        pygame.draw.line(self.screen, (0, 0, 0), (150, 0), (150, 450), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (300, 0), (300, 450), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 150), (450, 150), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 300), (450, 300), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 450), (450, 450), 5)

    def draw_mistakes(self):
        text_surface = self.font.render("Mistakes: " + str(self.mistake) + "/3", True, (255, 0, 0))
        text_rect = text_surface.get_rect(topleft = (10, self.window_height - 50))
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_board()
        self.draw_boundary_lines()
        self.draw_mistakes()

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            pygame.display.update()
            self.draw()
            self.clock.tick(60)


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

Game(grid).run()

'''
sudoku = Sudoku(grid)
solved = sudoku.solvedSudoku()
for i in solved:
    print(i)
print()
for i in grid:
    print(i)
'''

'''
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
'''

#print(solveSudoku(grid,0,0))
#for row in grid:
#   print(row)