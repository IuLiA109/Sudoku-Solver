import copy
import sys
import pygame
from Sudoku import Sudoku
from Board import Board

class Game:
    def __init__(self, board):
        pygame.init()
        pygame.display.set_caption('SUDOKU')
        self.original_board = copy.deepcopy(board)
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
        self.font = pygame.font.Font('assets/fonts/Arial.ttf', 25)
        self.pixel_font = pygame.font.Font('assets/fonts/Pixel.ttf', 25)

        self.state = "menu"
        self.menu_img = pygame.image.load('assets/images/menu_img.jpg')
        self.menu_img = pygame.transform.scale(self.menu_img, (self.window_width, self.window_height))

        self.win_img = pygame.image.load('assets/images/win.png')
        self.win_img = pygame.transform.scale(self.win_img, (self.window_width, self.window_height))

        self.lose_img = pygame.image.load('assets/images/sad.png')
        self.lose_img = pygame.transform.scale(self.lose_img, (self.window_width, self.window_height))

    def start_game(self):
        self.key = None
        self.click_column = None
        self.click_row = None
        self.mistake = 0
        self.board = Board(self.original_board)


    def handle_events_win(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.text_rect_back.collidepoint(x, y):
                    self.state = "menu"
    def handle_events_stop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.text_rect_back.collidepoint(x, y):
                    self.state = "menu"

    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.text_rect_play.collidepoint(x, y):
                    self.state = "playing"

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

            if event.type == pygame.KEYDOWN:
                self.key = None
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
                if self.key is not None:
                    if self.click_row is not None:
                        if self.solvedBoard[self.click_row][self.click_column] == self.key:
                            if self.board.board[self.click_row][self.click_column] == 0:
                                self.board.update(self.click_row, self.click_column, self.key)
                        else:
                            if self.mistake == 2:
                                self.state = "stop"
                                #pygame.quit()
                                #sys.exit()
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

    def draw_stop(self):
        self.screen.blit(self.lose_img, (0, 0))
        text_surface_lose = self.pixel_font.render("You lose!", True, (0, 0, 0))
        text_rect_lose = text_surface_lose.get_rect(center=(self.window_width // 2, self.window_height // 8))
        self.screen.blit(text_surface_lose, text_rect_lose)

        text_surface_back = self.pixel_font.render("BACK TO MENU", True, (0, 0, 0))
        self.text_rect_back = text_surface_back.get_rect(center=(self.window_width // 2, self.window_height - self.window_height // 9))
        self.screen.blit(text_surface_back, self.text_rect_back)

        pygame.display.flip()

    def draw_win(self):
        self.screen.blit(self.win_img, (0, 0))
        text_surface_win = self.pixel_font.render("Congratulations!", True, (0, 0, 0))
        text_rect_win = text_surface_win.get_rect(center=(self.window_width // 2, self.window_height // 8))
        self.screen.blit(text_surface_win, text_rect_win)

        text_surface_win = self.pixel_font.render("You've finished the game!", True, (0, 0, 0))
        text_rect_win = text_surface_win.get_rect(center=(self.window_width // 2, self.window_height // 8 + 25))
        self.screen.blit(text_surface_win, text_rect_win)

        text_surface_back = self.pixel_font.render("BACK TO MENU", True, (0, 0, 0))
        self.text_rect_back = text_surface_back.get_rect(center=(self.window_width // 2, self.window_height - self.window_height // 9))
        self.screen.blit(text_surface_back, self.text_rect_back)

        pygame.display.flip()

    def draw_menu(self):
        self.screen.blit(self.menu_img, (0, 0))
        text_surface_welcome = self.pixel_font.render("Welcome to Sudoku", True, (0, 0, 0))
        text_rect_welcome = text_surface_welcome.get_rect(center=(self.window_width // 2, self.window_height // 8))
        self.screen.blit(text_surface_welcome, text_rect_welcome)

        text_surface_play = self.pixel_font.render("PLAY", True, (0, 0, 0))
        self.text_rect_play = text_surface_play.get_rect(center=(self.window_width // 2, self.window_height - self.window_height // 8))
        self.screen.blit(text_surface_play, self.text_rect_play)

        pygame.display.flip()

    def solveSudoku_steps(self, row, column):
        if column == 9:
            if row == 8:
                return True
            row += 1
            column = 0
        if self.board.board[row][column] > 0:
            return self.solveSudoku_steps(row, column + 1)
        pygame.draw.rect(self.screen, self.board.cells[row][column]['color'], self.board.cells[row][column]['cell'])
        pygame.draw.rect(self.screen, (0, 0, 0), self.board.cells[row][column]['cell'], 2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.board.cells[row][column]['cell'], 2)
        self.draw_boundary_lines()

        for value in range(1, 10):
            if Sudoku(self.board.board).isValidSudoku(row, column, value):
                self.board.board[row][column] = value

                pygame.draw.rect(self.screen, self.board.cells[row][column]['color'], self.board.cells[row][column]['cell'])
                text_surface = self.font.render(str(value), True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(column * self.board.cell_size + self.board.cell_size // 2, row * self.board.cell_size + self.board.cell_size // 2))
                self.screen.blit(text_surface, text_rect)

                if value == self.solvedBoard[row][column]:
                    pygame.draw.rect(self.screen, (0, 0, 0), self.board.cells[row][column]['cell'], 2)
                    pygame.draw.rect(self.screen, (0, 255, 0), self.board.cells[row][column]['cell'], 2)
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), self.board.cells[row][column]['cell'], 2)
                    pygame.draw.rect(self.screen, (255, 0, 0), self.board.cells[row][column]['cell'], 2)

                pygame.display.flip()
                self.clock.tick(100)
                if self.solveSudoku_steps(row, column + 1):
                    pygame.draw.rect(self.screen, (255, 255, 255), self.board.cells[row][column]['cell'], 2)
                    pygame.draw.rect(self.screen, (0, 0, 0), self.board.cells[row][column]['cell'], 1)
                    self.draw_boundary_lines()
                    return True
                self.board.board[row][column] = 0
        return False

    def draw_solution(self):
        self.screen.fill((255, 255, 255))
        self.draw_board()
        self.draw_boundary_lines()
        self.solveSudoku_steps(0,0)
        self.state = "win"

        pygame.display.flip()

    def run(self):
        while True:
            if self.state == "menu":
                self.start_game()
                self.handle_events_menu()
                pygame.display.update()
                self.draw_menu()
            if self.state == "playing":
                self.handle_events()
                pygame.display.update()
                self.draw_solution()
                #self.draw()
            if self.state == "stop":
                self.handle_events_stop()
                pygame.display.update()
                self.draw_stop()
            if self.state == "win":
                self.handle_events_win()
                pygame.display.update()
                self.draw_win()
                # print("ok")
            if not self.board.exists_empty_cell() and self.state == "playing":
                self.state = "win"
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
