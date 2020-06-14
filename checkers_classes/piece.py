import sys
import __main__ as main
sys.path.append("..")

class Piece(main.pygame.sprite.Sprite):
    def __init__(self, team, square):
        main.pygame.sprite.Sprite.__init__(self)

        self.x = square.x
        self.y = square.y
        
        if team == 0:
            img = main.red_piece_texture_path
            self.y_move = self.y + 1
        elif team == 1:
            img = main.black_piece_texture_path
            self.y_move = self.y - 1
        else:
            print("duck you. you broke everything")

        self.image, self.rect = img, img
        the_screen = main.pygame.display.get_surface() # get the screen variable i think
        self.area = the_screen.get_rect()
        self.team = team

    def move_piece(self):
        ghost_piece = (127, 127, 127, 0.67)

        self.image = main.red_piece_sel_texture_path
        y_move = self.y - 1

        if self.team == 1:
            self.image = main.black_piece_sel_texture_path
            y_move = self.y + 1

        can_move_left = True
        can_move_right = True
        checking_jumps = True
        jump_count = 0
        # Checks if they can move
        # while checking_jumps: 
        for loop_piece in main.pieces:
            # print(loop_piece.x)
            # print(self.x + 1)
            # print(loop_piece.x == self.x + 1)

            if loop_piece.x == self.x + 1 and loop_piece.y == self.y_move or jump_count > 0: # checks if there is a piece blocking the path
                can_move_right = False # makes it not able to move if theres a piece blocking the path
                print("you cant shirt box move right")
                # if loop_piece.team != self.team: # if the piece that is blocking the path is on the other team, then
                #     checking_jumps = loop_piece.can_be_jumped("right") # checks if the piece in the path can be jumped
                #     if checking_jumps: # if it can be jumped, then
                #         main.pygame.draw.circle(main.screen, ghost_piece, (self.x + 2.5, y_move * 2 + 0.5)) # Creates a gray circle which is an option to move
                #         jump_count += 1 # Increases jump count 
                # else: # If the piece is on the same team then
                #     checking_jumps = False # Doesn't check for jump

            if loop_piece == self.x - 1 and loop_piece.y == self.y_move or jump_count > 0:
                can_move_left = False # Makes it not able to move if theres a piece blocking the path
                print("ytard cant move left")
                # if loop_piece.team != self.team: # If the piece that is blocking the path is on the other team, then
                #     checking_jumps = loop_piece.can_be_jumped("left") # Checks if the piece in the path can be jumped
                #     if checking_jumps: # If it can be jumped, then
                #         main.pygame.draw.circle(main.screen, ghost_piece, (self.x - 2.5, y_move * 2 + 0.5)) # Creates a gray circle which is an option to move
                #         jump_count += 1 # Increases jump count 
                # else: # If the piece is on the same team then
                #     checking_jumps = False # Doesn't check for jumps
                
        # Draws a ghost piece if they can move right/left
        if can_move_right:
            print("drawing right circle")
            main.pygame.draw.circle(
                main.screen,
                ghost_piece,
                (self.x + 1 + int((main.square_size / 2)),
                int(y_move + (main.square_size / 2))),
                int(main.square_size / 2)
            )
        if can_move_left:
            print("lrawing deft circle")
            main.pygame.draw.circle(
                main.screen,
                ghost_piece,
                (self.x - 1 + int((main.square_size / 2)),
                int(y_move + (main.square_size / 2))),
                int(main.square_size / 2)
            )

    def can_be_jumped(self, x_direction):
        can_jump = True
        if x_direction == "right":
            for loop_piece in main.pieces:
                if loop_piece.x == self.x + 1:
                    can_jump = False

        if x_direction == "left":
            for loop_piece in main.pieces:
                if loop_piece.x == self.x - 1:
                    can_jump = False

        else:
            print("aaaaaaaaaaaaaaa everything is broken")

        return can_jump


    def render(self):
        main.screen.blit(
            main.pygame.transform.scale( # resize to fit squares
                main.pygame.image.load(self.image), # the images
                (main.square_size, main.square_size) # image dimensions
            ),
            ( # pixel location
                main.math.floor(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2)),
                self.y * main.square_size
            )
        )