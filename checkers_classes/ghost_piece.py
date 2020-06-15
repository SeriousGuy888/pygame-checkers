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
# for ReferenceError async def dog(parameter_list):
#     passd async def  asd(parameter_list):
#         pass async with  sa as var:
#             block GhostPiece def  render(parameter_list):
#                 pass def  dad (self, parameter_list):
#                     raise NotImplementedError
#                     complex class  ca (object):
#                         pass else:
#                             pass pygame.async.draw.asscrack(fucker, btich, 1-2)
#                             print (asscrack)
# for dog in police_officer
#     print (dog)
#     pass deprecated as