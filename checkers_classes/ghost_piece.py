import sys
import __main__ as main
sys.path.append("..")

class GhostPiece(main.pygame.sprite.Sprite):
    def __init__(self, square):
        main.pygame.sprite.Sprite.__init__(self)

        self.x = square.x
        self.y = square.y


    def render(self):
        ghost_piece = (127, 127, 127)
        main.pygame.draw.circle(
            main.screen,
            ghost_piece,
            (
                int(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2) + (main.square_size / 2)),
                int((self.y * main.square_size) + (main.square_size / 2))
            ),
            int(main.square_size / 2)
        )