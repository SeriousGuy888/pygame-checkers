import sys
import __main__ as main
sys.path.append("..")

def override(f):
    return f

class KingPiece(main.piece.Piece):
    @override
    def move_piece(self):
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

                if loop_piece.x == self.x - 1 and loop_piece.y == self.backwards_y_move and can_move_right or jump_count > 0: # checks if there is a piece blocking the path
                    can_move_right = False # makes it not able to move if theres a piece blocking the path
                    print("you cant shirt box move right")
                    if loop_piece.team != self.team: # if the piece that is blocking the path is on the other team, then
                        checking_jumps = loop_piece.can_be_jumped("right", self.backwards_jump_y_move) # checks if the piece in the path can be jumped
                        if checking_jumps: # if it can be jumped, then
                            # main.pygame.draw.circle(main.screen, ghost_piece, (self.x + 2.5, y_move * 2 + 0.5)) # Creates a gray circle which is an option to move
                            jump_count += 1 # Increases jump count 

                if loop_piece.x == self.x + 1 and loop_piece.y == self.backwards_y_move or jump_count > 0:
                    can_move_left = False # Makes it not able to move if theres a piece blocking the path
                    print("ytard cant move left")
                    if loop_piece.team != self.team: # If the piece that is blocking the path is on the other team, then
                        checking_jumps = loop_piece.can_be_jumped("left", self.backwards_jump_y_move) # Checks if the piece in the path can be jumped
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
            # print("drawing right circle")
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
                if loop_square.x == self.x - 1 and loop_square.y == self.y_move:
                    print("x = " + str(loop_square.x))
                    print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square))