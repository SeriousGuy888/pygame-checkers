
import sys
import ctypes
import math
import random
from pathlib import Path
import pygame

from pygame import mixer

from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

from checkers_classes import piece
from checkers_classes import ghost_piece
from checkers_classes import square

user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

pygame.init() # actual game

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # screen size and stuffs
pygame.display.set_caption("Donut Checkers")

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

roboto_bold = "./assets/fonts/Roboto-Bold.ttf"

# * red down; black up


dogshit = ["dog", "shirt", "this is an easter egg that no one will find unless there's dog in 🌈"]

pieces = []
king_pieces = []
ghost_pieces = []
squares = []
jumped_pieces = []

turn = 1
winner = 2

def spawn_sprites():
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

def remove_sprites():
    sprites = [pieces, king_pieces, ghost_pieces, squares, jumped_pieces]

    for sprite in sprites:
        sprite.clear()

def show_text(font_file, font_size, text_colour, coords, string):
    font = pygame.font.Font(font_file, font_size)

    text = font.render(string, True, text_colour)
    text_rect = text.get_rect()
    text_rect.center = (x, y) = coords

    return {"text": text, "rect": text_rect}

def clamp(number, minimum, maximum):
    val = number
    if number < minimum: val = minimum
    if number > maximum: val = maximum
    return val

def main():
    RUNNING = True # running variable - will be set to false when x is pressed, quitting the program
    game_state = 0
    ticks = 0

    while RUNNING: # main game loop
        pygame.display.update()
        pygame.display.flip() # display the display to the display

        ticks += 1 # increments the game's tick counter also apparently python has no ++ incrementor

        screen.blit(background_image, (0, 0)) # display background image

        for event in pygame.event.get(): # process every event
            if event.type == KEYDOWN: # detect key presses
                if game_state == 0:
                    if event.key == K_SPACE:
                        game_state = 1
                        spawn_sprites()
                    if event.key == K_ESCAPE:
                        RUNNING = False
                if game_state == 1:
                    if event.key == K_ESCAPE:
                        game_state = 0
                        remove_sprites()
            if event.type == QUIT: # press quit
                RUNNING = False # kills stuffs :D

        if game_state == 0:
            boring_colour = (200, 200, 200)
            start_colour = (
                clamp(200 + (ticks % 50 * 2), 0, 255),
                clamp(200 + (ticks % 50 * 4), 0, 255),
                clamp(200 + (ticks % 50 * 6), 0, 255)
            )

            title_y = SCREEN_HEIGHT // 3

            title = show_text(roboto_bold, 128, boring_colour, (SCREEN_WIDTH // 2, title_y), "Donut Checkers")
            start = show_text(roboto_bold, 48, start_colour, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 * 2), "Press SPACE to play")
            exiting = show_text(roboto_bold, 48, boring_colour, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 * 2 + 100), "Press ESC to exit")
            buttons = show_text(roboto_bold, 48, boring_colour, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 * 2 + 150), "(because I'm too lazy to make buttons)")

            screen.blit(title["text"], title["rect"])
            screen.blit(start["text"], start["rect"])
            screen.blit(exiting["text"], exiting["rect"])
            screen.blit(buttons["text"], buttons["rect"])
        if game_state == 1:
            for loop_square in squares: # process all the squares
                loop_square.render()

            if winner not in (0, 1):
                for loop_piece in pieces: # process all the pieces
                    loop_piece.render()
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
                        loop_piece.team == turn and
                        not loop_piece.selected
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

            # pieces[3].move_piece()
            
            if winner == 0:
                screen.blit(
                    pygame.transform.scale( # resize to fit squares
                        pygame.image.load("assets/textures/donut_monster/red_donut_monster_with_trophy.png"), # the images
                        (square_size * 4, square_size * 8) # image dimensions
                    ),
                    ( # pixel location
                        int(SCREEN_WIDTH / 2 - (square_size * 2)),
                        square_size
                    )
                )
            
            elif winner == 1:
                screen.blit(
                    pygame.transform.scale( # resize to fit squares
                        pygame.image.load("assets/textures/donut_monster/black_donut_monster_with_trophy.png"), # the images
                        (square_size * 4, square_size * 8) # image dimensions
                    ),
                    ( # pixel location
                        int(SCREEN_WIDTH / 2 - (square_size * 4)),
                        square_size
                    )
                )
            
            # print(f"Ghost piece count: {len(ghost_pieces)}")


main()
sys.exit()
