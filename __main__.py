import ctypes
import sys
import pygame

from pygame.locals import *

user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

pygame.init() # actual game

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # screen size and stuffs


RUNNING = True # running variable - will be set to false when x is pressed, quitting the program

while RUNNING:
    for event in pygame.event.get():
        if event.type == KEYDOWN: # detect key presses
            if event.key == K_ESCAPE: # detect esc
                RUNNING = False # quit
        if event.type == QUIT: # press quit
            RUNNING = False # kills stuffs :D



    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), [20, 20, 20, 20])
    pygame.display.update()

    pygame.display.flip() # display the display to the display

sys.exit()