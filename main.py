import sys
import pygame

class Board:
    def __init__(self, board):
        pygame.init()
        pygame.display.set_caption('SUDOKU')
        self.screen = pygame.display.set_mode((450, 500))
        self.clock = pygame.time.Clock()

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

        self.font = pygame.font.Font(None, 30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = x // self.cell_size # width c
                y = y // self.cell_size # height l
                if self.board[y][x] != 0:
                    for i in range(len(self.cells)):
                        for j in range(len(self.cells[i])):
                            if y == i or x == j or (y//3 == i//3 and x//3 == j//3):
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


    def draw_board(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                x = i * self.cell_size
                y = j * self.cell_size
                pygame.draw.rect(self.screen, self.cells[i][j]['color'], self.cells[i][j]['cell'])
                pygame.draw.rect(self.screen, (0, 0, 0), self.cells[i][j]['cell'], 1)
                if self.board[i][j] != 0:
                    text_surface = self.font.render(str(self.board[i][j]), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center = (y + self.cell_size // 2, x + self.cell_size // 2))
                    self.screen.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_board()
        pygame.draw.line(self.screen, (0, 0, 0), (150, 0), (150, 450), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (300, 0), (300, 450), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 150), (450, 150), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 300), (450, 300), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 450), (450, 450), 5)
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

Board(grid).run()


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

#print(solveSudoku(grid,0,0))
#for row in grid:
#   print(row)