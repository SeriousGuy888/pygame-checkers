import sys
sys.path.append("..")
import __main__ as main

class Piece(main.pygame.sprite.Sprite):
    def __init__(self, team, x, y):
        main.pygame.sprite.Sprite.__init__(self)
        
        if team == 0:
            img = main.red_piece_texture_path
        elif team == 1:
            img = main.black_piece_texture_path
        else:
            print("fuck you. you broke everything")

        self.image, self.rect = img, img
        the_screen = main.pygame.display.get_surface() # get the screen variable i think
        self.area = the_screen.get_rect()
        self.team = team
        self.x = x
        self.y = y

    def move_piece(self):
        self.image = main.red_piece_sel_texture_path
        y_move = self.y - main.square_size

        if self.team == 1:
            self.image = main.black_piece_sel_texture_path
            y_move = self.y + main.square_size

        can_move_left = True
        can_move_right = True
        can_jump_left = False
        can_jump_right = False
            
        # Checks if they can move 
        for loop_piece in main.pieces:
            if loop_piece.x == self.x + square_size:
                can_move_right = False
                if loop_piece.team != self.team:
                    pass
                    # TODO: somehow figure out if this can jump

            elif loop_piece == self.x - square_size:
                can_move_left = False

            
            # Draws a grey circle if they can move right/left
            if can_move_right:
                main.pygame.draw.circle(main.screen, (127, 127, 127), (self.x + main.square_size, y_move))
            if can_move_left:
                main.pygame.draw.circle(main.screen, (127, 127, 127), (self.x - main.square_size, y_move))
        
    def render(self):
        main.screen.blit(main.pygame.transform.scale(main.pygame.image.load(self.image), (main.square_size, main.square_size)), (self.x * main.square_size, self.y * main.square_size))