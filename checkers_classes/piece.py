import sys
import __main__ as main
# import "../checkers_classes/ghost_piece" as ghost_piece
sys.path.append("..")

class Piece(main.pygame.sprite.Sprite):
    def __init__(self, team, square):
        main.pygame.sprite.Sprite.__init__(self)

        self.x = square.x
        self.y = square.y
        
        if team == 0:
            img = main.red_piece_texture_path
            self.y_move = self.y + 1 # y_move is the y direction the piece can move. It's saved as the y it can go to on a move
            self.jump_y_move = self.y + 2 # This is y_move but for jumping
            self.backwards_y_move = self.y - 1
            self.backwards_jump_y_move = self.y - 2
        elif team == 1:
            img = main.black_piece_texture_path
            self.y_move = self.y - 1 # y_move is the y direction the piece can move. It's saved as the y it can go to on a move
            self.jump_y_move = self.y - 2 # This is y_move but for jumping
            self.backwards_y_move = self.y + 1
            self.backwards_jump_y_move = self.y + 2
        else:
            print("duck you. you broke everything")

        self.image, self.rect = img, img
        the_screen = main.pygame.display.get_surface() # get the screen variable i think
        self.area = the_screen.get_rect()
        self.team = team

    def move_piece(self):
        # ghost_piece = (127, 127, 127, 0.67)
        print(self.x)
        print(self.y)

        self.image = main.red_piece_sel_texture_path

        if self.team == 1:
            self.image = main.black_piece_sel_texture_path

        can_move_left = self.x < 8 # As long as it isn't on the far left it defaults to being able to move left
        can_move_right = self.x > 1 # As long as it isn't on the far right it defaults to being able to move right
        checking_jumps = True # This is so the while loop will go around the fist time
        jump_count = 0 # No jumps have happened yet
        # Checks if they can move
        while checking_jumps: 
            for loop_piece in main.pieces:

                if loop_piece.x == self.x - 1 and loop_piece.y == self.y_move and can_move_right or jump_count > 0: # checks if there is a piece blocking the path
                    can_move_right = False # makes it not able to move if theres a piece blocking the path
                    print("you cant shirt box move right")
                    if loop_piece.team != self.team: # if the piece that is blocking the path is on the other team, then
                        checking_jumps = loop_piece.can_be_jumped("right", self.jump_y_move) # checks if the piece in the path can be jumped
                        if checking_jumps: # if it can be jumped, then
                            # main.pygame.draw.circle(main.screen, ghost_piece, (self.x + 2.5, y_move * 2 + 0.5)) # Creates a gray circle which is an option to move
                            jump_count += 1 # Increases jump count 

                if loop_piece.x == self.x + 1 and loop_piece.y == self.y_move or jump_count > 0:
                    can_move_left = False # Makes it not able to move if theres a piece blocking the path
                    print("ytard cant move left")
                    if loop_piece.team != self.team: # If the piece that is blocking the path is on the other team, then
                        checking_jumps = loop_piece.can_be_jumped("left", self.jump_y_move) # Checks if the piece in the path can be jumped
                        if checking_jumps: # If it can be jumped, then
                            # main.pygame.draw.circle(main.screen, ghost_piece, (self.x - 2.5, y_move * 2 + 0.5)) # Creates a gray circle which is an option to move
                            jump_count += 1 # Increases jump count 

                else: # If there aren't any pieces in its path don't keep checking for jumps
                    checking_jumps = False # Doesn't check for jumps
                
        # Draws a ghost piece if they can move right/left
        if can_move_right:
            for loop_square in main.squares:
                if loop_square.x == self.x - 1 and loop_square.y == self.y_move:
                    print("x = " + str(loop_square.x))
                    print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square))
            print("drawing right circle")
            # print(int(y_move * main.square_size) + 2)

            # x_coord = 0
            # y_coord = 0
            # for square in main.squares:
            #     if square.x == self.x * 3 and square.y == self.y * 3:
            #         x_coord = square.x
            #         y_coord = square.y
                    
            # main.pygame.draw.circle(
            #     main.screen,
            #     ghost_piece,
            #     (
            #         x_coord * main.square_size,
            #         y_coord * main.square_size
            #     ), # y
            #     int(main.square_size / 2) # radius
            # )
        if can_move_left:
            for loop_square in main.squares:
                if loop_square.x == self.x + 1 and loop_square.y == self.y_move:
                    print("x = " + str(loop_square.x))
                    print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square))
            print("lrawing deft circle")
            # main.pygame.draw.circle(
            #     main.screen,
            #     ghost_piece,
            #     (self.x - 1 + int((main.square_size / 2)),
            #     int(y_move + (main.square_size / 2))),
            #     int(main.square_size / 2)
            # )

    def can_be_jumped(self, x_direction, jumper_y_move):
        can_jump = True # Set the default to it being able to be jumped
        if x_direction == "right": # If it's being jumped to the right
            for loop_piece in main.pieces: # Check each piece
                if loop_piece.x == self.x + 1: # If there's a piece blocking the jump
                    can_jump = False # It can't be jumped
                    print("cant be jumped right") # This was for debugging and I might delete it

        if x_direction == "left": # Same as above but for jumping to the left
            for loop_piece in main.pieces:
                if loop_piece.x == self.x - 1 and loop_piece.y == jumper_y_move:
                    can_jump = False
                    print("cant be jumped left")

        else: # This is mostly for debugging but maybe I'll do something else with it
            print("is able to be jumped" + x_direction)

        return can_jump # If it doesn't think there's anything blocking the jump it'll return the default but if it's changed to False it'll return that


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