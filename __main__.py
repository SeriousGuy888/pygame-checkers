
import sys
import ctypes
import math
import random
from pathlib import Path
import pygame

from pygame import mixer

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



# * non-functional function
# def mouse_overlapping(x, y, width, height, mouse_x, mouse_y):
#     if(
#         (x - 1) * width < mouse_x and
#         x * width > mouse_x and
#         y * height < mouse_y and
#         (y + 1) * height > mouse_y
#     ):
#         return True
#     else:
#         return False

def get_directory_files(directory, search_pattern):
    paths = Path(directory).glob(search_pattern)
    files = []
    for path in paths:
        files.append(str(path))
    return files

def load_sounds_from_files(path_list):
    sounds = []
    for path in path_list:
        sounds.append(pygame.mixer.Sound(path))
    return sounds


white_square = (209, 168, 107)
black_square = (135, 89, 19)
square_size = math.floor(SCREEN_HEIGHT / 10)
SQUARE_DIMENSION = 8

board_x_offset = int(SCREEN_WIDTH / 2 - (square_size * (SQUARE_DIMENSION / 2 + 1)))

background_image = pygame.image.load("./assets/textures/table.png")

red_piece_texture_path = "./assets/textures/pieces/normal/red_piece.png"
black_piece_texture_path = "./assets/textures/pieces/normal/black_piece.png"
red_king_piece_texture_path = "./assets/textures/pieces/normal/king_red_piece.png"
black_king_piece_texture_path = "./assets/textures/pieces/normal/king_black_piece.png"

red_piece_sel_texture_path = "./assets/textures/pieces/selected/sel_red_piece.png"
black_piece_sel_texture_path = "./assets/textures/pieces/selected/sel_black_piece.png"
red_king_piece_sel_texture_path = "./assets/textures/pieces/selected/sel_king_red_piece.png"
black_king_piece_sel_texture_path = "./assets/textures/pieces/selected/sel_king_black_piece.png"

ghost_piece_texture_path = "./assets/textures/pieces/ghost/ghost_piece.png"

red_donut_monster = "./assets/textures/donut_monster/red_donut_monster_with_trophy.png"
black_donut_monster = "./assets/textures/donut_monster/black_donut_monster_with_trophy.png"



move_sounds = load_sounds_from_files(get_directory_files("./assets/sfx/move", "*.wav"))


# * red down; black up


dogshit = ["dog", "shirt", "this is an easter egg that no one will find unless there's dog in 🌈"]

pieces = []
king_pieces = []
ghost_pieces = []
squares = []
jumped_pieces = []
turn = 1
winner = 2

def main():
    RUNNING = True # running variable - will be set to false when x is pressed, quitting the program
    for x in range(1, SQUARE_DIMENSION + 1):
        for y in range(1, SQUARE_DIMENSION + 1):
            if (x + (1 - y % 2)) % 2 == 1:
                square_colour = white_square
            if (x + (1 - y % 2)) % 2 == 0:
                square_colour = black_square

            # print(x, y)
            squares.append(square.Square(square_colour, x, y))

    for x in range(1, 8, 2):
        for y in [1, 2, 3, 6, 7, 8]:
            x_coord = x + (y % 2)
            y_coord = y
            team = 0 if y < 5 else 1 
            for loop_square in squares:
                if loop_square.x == x_coord and loop_square.y == y_coord:
                    pieces.append(piece.Piece(team, loop_square, False))
    
    # for x in range(2, 7):
    #     for y in range(3, 6):
    #         for loop_square in squares:
    #             if loop_square.x == x and loop_square.y == y:
    #                 pieces.append(ghost_piece.GhostPiece(loop_square))
    
    # pieces[3].move_piece()

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
        

        # mouse_collide = pygame.sprite.spritecollide
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos_x, mouse_pos_y = mouse_pos


        if mouse_pressed[0]:
            global turn
            for loop_piece in pieces:
                if(
                    loop_piece.x * square_size + board_x_offset < mouse_pos_x and
                    (loop_piece.x + 1) * square_size + board_x_offset > mouse_pos_x and
                    loop_piece.y * square_size < mouse_pos_y and
                    (loop_piece.y + 1) * square_size > mouse_pos_y and
                    loop_piece.team == turn
                ):
                    loop_piece.move_piece()

            for loop_ghost_piece in ghost_pieces:
                if(
                    loop_ghost_piece.x * square_size + board_x_offset < mouse_pos_x and
                    (loop_ghost_piece.x + 1) * square_size + board_x_offset > mouse_pos_x and
                    loop_ghost_piece.y * square_size < mouse_pos_y and
                    (loop_ghost_piece.y + 1) * square_size > mouse_pos_y
                ):
                    pygame.mixer.Sound.play(random.choice(move_sounds))
                    turn = [1, 0][loop_piece.team]
                    loop_ghost_piece.move_ghosted_piece()
        

        for event in pygame.event.get(): # process every event
            if event.type == KEYDOWN: # detect key presses
                if event.key == K_ESCAPE: # detect esc
                    RUNNING = False # quit
            if event.type == QUIT: # press quit
                RUNNING = False # kills stuffs :D

        # pieces[3].move_piece()

        # print(f"Ghost piece count: {len(ghost_pieces)}")

        pygame.display.update()
        pygame.display.flip() # display the display to the display


main()
sys.exit()
