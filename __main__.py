import ctypes
import math
import sys
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from checkers_classes import piece
from checkers_classes import square

user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

pygame.init() # actual game

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # screen size and stuffs
pygame.display.set_caption("Caption")




RUNNING = True # running variable - will be set to false when x is pressed, quitting the program



white_square = (209, 168, 107)
black_square = (135, 89, 19)
square_size = math.floor(SCREEN_HEIGHT / 10)
SQUARE_DIMENSION = 8

background_image = pygame.image.load("./assets/table.png")
red_piece_texture_path = "./assets/red_piece.png"
red_piece_sel_texture_path = "./assets/glowing_red_piece.png"
black_piece_texture_path = "./assets/black_piece.png"
black_piece_sel_texture_path = "./assets/glowing_black_piece.png"



# * red down; black up


dogshit = ["dog", "shit", "this is an easter egg that no one will find unless there's dog in 🌈"]

pieces = []
squares = []

def main():
    for x in range(1, SQUARE_DIMENSION + 1):
        for y in range(1, SQUARE_DIMENSION + 1):
            if (x + (y % 2)) % 2 == 1:
                square_colour = white_square
            if (x + (y % 2)) % 2 == 0:
                square_colour = black_square

            squares.append(square.Square(square_colour, x, y))

    for x in range(1, 8, 2):
        for y in range(1, 4):
            pieces.append(piece.Piece(0, x + (y % 2), y))
    for x in range(1, 8, 2):
        for y in range(6, 9):
            pieces.append(piece.Piece(1, x + (y % 2), y))
main()

while RUNNING:
    for event in pygame.event.get():
        if event.type == KEYDOWN: # detect key presses
            if event.key == K_ESCAPE: # detect esc
                RUNNING = False # quit
        if event.type == QUIT: # press quit
            RUNNING = False # kills stuffs :D


    screen.blit(background_image, (0, 0))
    for square in squares:
        square.render()
    for piece in pieces:
        piece.render()

    pygame.display.update()
    pygame.display.flip() # display the display to the display

sys.exit()