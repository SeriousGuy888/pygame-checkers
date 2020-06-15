import sys
import __main__ as main
sys.path.append("..")

class Square(main.pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        main.pygame.sprite.Sprite.__init__(self)

        self.colour = colour
        self.x = x
        self.y = y
    def render(self):
        main.pygame.draw.rect(main.screen, self.colour, [
            int(main.SCREEN_WIDTH/2 - (main.square_size * 5) + (self.x * main.square_size)),
            main.square_size * self.y,
            main.square_size,
            main.square_size
        ])