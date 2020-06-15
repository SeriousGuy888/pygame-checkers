
import sys
import ctypes
import math
import random
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

from checkers_classes import piece
from checkers_classes import king_piece
from checkers_classes import ghost_piece
from checkers_classes import square

user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

pygame.init() # actual game

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # screen size and stuffs
pygame.display.set_caption("Donut Checkers")



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


dogshit = ["dog", "shirt", "this is an easter egg that no one will find unless there's dog in 🌈"]

pieces = []
king_pieces = []
ghost_pieces = []
squares = []

def main():
    RUNNING = True # running variable - will be set to false when x is pressed, quitting the program
    for x in range(1, SQUARE_DIMENSION + 1):
        for y in range(1, SQUARE_DIMENSION + 1):
            if (x + (y % 2)) % 2 == 1:
                square_colour = white_square
            if (x + (y % 2)) % 2 == 0:
                square_colour = black_square

            # print(x, y)
            squares.append(square.Square(square_colour, x, y))

    for x in range(1, 8, 2):
        for y in [1, 2, 3, 6, 7, 8]:
            x_coord = x + (1 - (y % 2))
            y_coord = y
            team = 0 if y < 5 else 1 
            for loop_square in squares:
                if loop_square.x == x_coord and loop_square.y == y_coord:
                    pieces.append(piece.Piece(team, loop_square))
    
    # for x in range(2, 7):
    #     for y in range(3, 6):
    #         for loop_square in squares:
    #             if loop_square.x == x and loop_square.y == y:
    #                 pieces.append(ghost_piece.GhostPiece(loop_square))
    
    pieces[3].move_piece()

    while RUNNING: # main game loop
        screen.blit(background_image, (0, 0)) # display background image
        for loop_square in squares: # process all the squares
            loop_square.render()
        for loop_piece in pieces: # process all the pieces
            loop_piece.render()
        for loop_king_piece in king_pieces: # process all the king pieces
            loop_king_piece.render()
        for loop_ghost_piece in ghost_pieces: # process all the ghost pieces
            loop_ghost_piece.render()
        


        mouse_collide = pygame.sprite.spritecollide
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            if mouse_collide(piece, piece.Piece, True) and mouse_pressed[0]:
                pygame.draw.circle(screen, (255, 255, 255), mouse_pos, 25)
        

        for event in pygame.event.get(): # process every event
            if event.type == KEYDOWN: # detect key presses
                if event.key == K_ESCAPE: # detect esc
                    RUNNING = False # quit
            if event.type == QUIT: # press quit
                RUNNING = False # kills stuffs :D

        # pieces[3].move_piece()

        pygame.display.update()
        pygame.display.flip() # display the display to the display


main()
sys.exit()