import pygame

board_width = 9
board_height = 9
cell_size = 70

window_width = board_width * cell_size + 4 * cell_size
window_height = board_height * cell_size + 4 * cell_size

font = pygame.font.Font('assets/fonts/Arial.ttf', 25)
small_font = pygame.font.Font('assets/fonts/Arial.ttf', 21)
notes_font = pygame.font.Font('assets/fonts/Arial.ttf', 21)
pixel_font = pygame.font.Font('assets/fonts/Pixel.ttf', 25)

hint_image = pygame.image.load("assets/images/hint.png")
hint_image = pygame.transform.scale(hint_image, (32, 50))

solve_image = pygame.image.load("assets/images/solve.png")
solve_image = pygame.transform.scale(solve_image, (54, 50))

note_img = pygame.image.load('assets/images/note.png')
note_img = pygame.transform.scale(note_img, (64, 50))

erase_img = pygame.image.load('assets/images/erase.png')
erase_img = pygame.transform.scale(erase_img, (71, 50))

menu_img = pygame.image.load('assets/images/menu_img.jpg')
menu_img = pygame.transform.scale(menu_img, (window_width, window_height))

win_img = pygame.image.load('assets/images/win.png')
win_img = pygame.transform.scale(win_img, (window_width, window_height))

lose_img = pygame.image.load('assets/images/sad.png')
lose_img = pygame.transform.scale(lose_img, (window_width, window_height))
