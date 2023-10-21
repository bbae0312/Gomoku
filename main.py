import pygame
from gomoku import *

# Initialization
pygame.init()
SURFACE = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

# Variables
black_turn = True
running = True
is_down = False
is_valid = False
new_pos = (0, 0)
win = None

def handle_mouse_up():
    global is_down, black_turn, running, win
    is_valid, i_new, j_new = checkValid(pygame.mouse.get_pos())
    if is_valid:
        is_down = False
        if board[i_new][j_new] == NO_DOL:
            board[i_new][j_new] = BLACK_DOL if black_turn else WHITE_DOL
            dols_order.append((i_new, j_new, board[i_new][j_new]))
            printBoard()
            if checkOmok(i_new, j_new, black_turn):
                running = False
                win = board[i_new][j_new]
            black_turn = not black_turn

def display_winner():
    win_text = "Black Stone" if win == BLACK_DOL else "White Stone"
    win_text += " Wins!"
    text_surface = myfont.render(win_text, False, (0, 0, 255))
    SURFACE.blit(text_surface, (w // 2 - 200, h // 2 - font_size))
    pygame.display.update()
    for _ in range(6):
        clock.tick(1)

# Main Game Loop
while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONDOWN:
            is_down = True
        elif e.type == MOUSEBUTTONUP:
            handle_mouse_up()

    # Drawing
    SURFACE.fill(YELLOW)
    draw_board(SURFACE)
    draw_dols_order(SURFACE, 0, len(dols_order))
    pygame.display.update()
    clock.tick(30)

# Game End
if win:
    display_winner()

pygame.quit()
