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
                main.pygame.image.load(main.ghost_piece_texture_path), # the images
                (main.square_size, main.square_size) # image dimensions
            ),
            ( # pixel location
                # int(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2)),
                int(main.SCREEN_WIDTH / 2 - (main.square_size * 5) + (self.x * main.square_size)),
                self.y * main.square_size
            )
        )