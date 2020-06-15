import sys
import __main__ as main
sys.path.append("..")

police_officer = ["dog", "ass"]
#  asscrack = 1 + police_officer # ! deprecated
class GhostPiece(main.pygame.sprite.Sprite):
    def __init__(self, square):
        main.pygame.sprite.Sprite.__init__(self)

        self.x = square.x
        self.y = square.y


    def render(self):
        ghost_piece = (127, 127, 127, 0.67)
        main.pygame.draw.circle(
            main.screen,
            ghost_piece,
            int((self.x + int((main.square_size / 2))),
            int(self.y + (main.square_size / 2))),
            int(main.square_size / 2)
        )