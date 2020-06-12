import ctypes
import math
import sys
import pygame

from pygame.locals import *

user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

pygame.init() # actual game

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # screen size and stuffs


RUNNING = True # running variable - will be set to false when x is pressed, quitting the program



class Piece:
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = pygame.image.load("./assets/red_piece.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector



background_image = pygame.image.load("./assets/table.png")
white_square = (209, 168, 107)
black_square = (135, 89, 19)
square_size = math.floor(SCREEN_HEIGHT / 10)
SQUARE_DIMENSION = 8

while RUNNING:
    for event in pygame.event.get():
        if event.type == KEYDOWN: # detect key presses
            if event.key == K_ESCAPE: # detect esc
                RUNNING = False # quit
        if event.type == QUIT: # press quit
            RUNNING = False # kills stuffs :D



    screen.blit(background_image, (0, 0))
    for i in range(1, SQUARE_DIMENSION + 1):
        for j in range(1, SQUARE_DIMENSION + 1):
            sqCalc = i
            if j % 2 == 0:
                sqCalc += 1

            if sqCalc % 2 == 1:
                square_colour = white_square
            if sqCalc % 2 == 0:
                square_colour = black_square

            pygame.draw.rect(screen, square_colour, [
                SCREEN_WIDTH - ((square_size * i) + ((SCREEN_WIDTH - (square_size * 8)) / 2)),
                square_size * j,
                square_size,
                square_size
            ])
            
    pygame.display.update()
    pygame.display.flip() # display the display to the display

sys.exit()