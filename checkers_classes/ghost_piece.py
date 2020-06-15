import sys
import __main__ as main
sys.path.append("..")

class GhostPiece(main.pygame.sprite.Sprite):
    def __init__(self, square):
        main.pygame.sprite.Sprite.__init__(self)

        self.x = square.x
        self.y = square.y


    def render(self):
        main.screen.blit(
            main.pygame.transform.scale( # resize to fit squares
                main.pygame.image.load("assets/ghost_piece.png"), # the images
                (main.square_size, main.square_size) # image dimensions
            ),
            ( # pixel location
                int(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2)),
                self.y * main.square_size
            )
        )