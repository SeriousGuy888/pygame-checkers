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
pygame.display.set_caption("Caption")


RUNNING = True # running variable - will be set to false when x is pressed, quitting the program


background_image = pygame.image.load("./assets/table.png")
white_square = (209, 168, 107)
black_square = (135, 89, 19)
square_size = math.floor(SCREEN_HEIGHT / 10)
SQUARE_DIMENSION = 8

# * red down; black up

class Piece(pygame.sprite.Sprite):
    def __init__(self, team, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        if team == 0:
            img = "./assets/red_piece.png"
        elif team == 1:
            img = "./assets/black_piece.png"
        else:
            print("fuck you. you broke everything")

        self.image, self.rect = img, img
        the_screen = pygame.display.get_surface() # get the screen variable i think
        self.area = the_screen.get_rect()
        self.team = team
        self.x = x
        self.y = y

    def move_piece(self):
        self.image = "./assets/glowing_red_piece.png"
        y_move = self.y - square_size

        if self.team == 1:
            self.image = "./assets/glowing_black_piece.png"
            y_move = self.y + square_size

        can_move_left = True
        can_move_right = True
        can_jump_left = False
        can_jump_right = False
            
            # Checks if they can move 
        for loop_piece in pieces:
            if loop_piece.x == self.x + square_size:
                can_move_right = False
                if loop_piece.team != self.team:
                    pass
                    # TODO: somehow figure out if this can jump

            elif loop_piece == self.x - square_size:
                can_move_left = False

            
            #  Draws a grey circle if they can move right/left
            if can_move_right:
                pygame.draw.circle(screen, (127, 127, 127), (self.x + square_size, y_move))
            if can_move_left:
                pygame.draw.circle(screen, (127, 127, 127), (self.x - square_size, y_move))
        
    def render(self):
        screen.blit(pygame.transform.scale(pygame.image.load(self.image), (square_size, square_size)), (self.x * square_size, self.y * square_size))

class Square(pygame.sprite.Sprite):
    def __init__(self, square_colour, x, y):
        self.square_colour == square_colour
        self.x = x
        self.y = y
    def render(self):
        pygame.draw.rect(screen, square_colour, [
            square_size * self.x,
            square_size * self.y,
            square_size,
            square_size
        ])


pieces = []
squares = []
dogshit = ["dog", "shit", "this is an easter egg that no one will find unless there's dog in 🌈"]

def main():
    print("")
    for y in range(1, 4):
        for x in range(1, 8, 2):
            pieces.append(Piece(0, x + 4 + (y % 2), y))
    for y in range(6, 9):
        for x in range(1, 8, 2):
            pieces.append(Piece(1, x + 4 + (y % 2), y))


main()

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
            if j % 2 == 1:
                sqCalc += 1

            if sqCalc % 2 == 1:
                square_colour = white_square
            if sqCalc % 2 == 0:
                square_colour = black_square

            pygame.draw.rect(screen, square_colour, [
                math.floor(SCREEN_WIDTH - (square_size * i) - ((SCREEN_WIDTH - (square_size * 8)) / 2)),
                square_size * j,
                square_size,
                square_size
            ])

    for piece in pieces:
        piece.render()

    pygame.display.update()
    pygame.display.flip() # display the display to the display

sys.exit()