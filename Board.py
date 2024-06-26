import copy
import random
import pygame

class Board:
    def __init__(self, board):
        self.board_width = 9
        self.board_height = 9
        self.cell_size = 70
        self.board = copy.deepcopy(board)
        self.emptyCells = [[r, c] for r in range(self.board_height) for c in range(self.board_width) if self.board[r][c] == 0]
        self.notes = [[set() for _ in range(self.board_width)] for _ in range(self.board_height)]

        self.cells = []
        for i in range(self.board_height):
            aux = []
            for j in range(self.board_width):
                x = i * self.cell_size + self.cell_size #???????????
                y = j * self.cell_size + self.cell_size
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

    def unclickCells(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.cells[i][j]['color'] = (255, 255, 255)

    def randomCell(self):
        random_number = random.randint(0, len(self.emptyCells) - 1)
        return self.emptyCells[random_number][0], self.emptyCells[random_number][1]

    def update(self, row, column, value):
        self.board[row][column] = value

    def exists_empty_cell(self):
        if len(self.emptyCells) == 0:
            return False
        return True
    '''
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.board[i][j] == 0:
                    return True
        return False
    '''
