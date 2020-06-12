import sys
import ctypes
import pygame

from pygame.locals import *

user32 = ctypes.windll.user32
screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# kekw XD
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75, 25))
#         self.surf.fill((255, 255, 255))
#         self.rect = self.surf.get_rect()
py.

pygame.init()

screen = pygame.display.set_mode(screen_size)
# player = Player()
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == KEYDOWN: # detect key presses
            if event.key == K_ESCAPE: # detect esc
                RUNNING = False # quit
        if event.type == QUIT: # press quit bitch
            RUNNING = False # kills stuffs :D

    screen.fill((25, 25, 25))
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    pygame.display.flip() # display the display to the display

sys.exit()
