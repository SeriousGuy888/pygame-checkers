import sys
sys.path.append("..")
import __main__ as main

class Square(main.pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        main.pygame.sprite.Sprite.__init__(self)

        self.colour = colour
        self.x = x
        self.y = y
    def render(self):
        main.pygame.draw.rect(main.screen, self.colour, [
            main.math.floor(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2)),
            main.square_size * self.y,
            main.square_size,
            main.square_size
        ])