import __main__ as main

class Piece(main.pygame.sprite.Sprite):
    def __init__(self, team, square, selected):
        main.pygame.sprite.Sprite.__init__(self)

        self.square = square
        self.x = square.x
        self.y = square.y
        self.team = team

        self.selected = selected
            
        img = [main.red_piece_texture_path, main.black_piece_texture_path][self.team] # chooses image based on team
        
        self.y_move = self.y + (1 - (self.team * 2)) # what the piece's y would be when it moves
        self.jump_y_move = self.y_move + (1 - (self.team * 2)) # jump version
        self.backwards_y_move = self.y + (-1 + (self.team * 2)) # backwards version
        self.backwards_jump_y_move = self.backwards_y_move + (-1 + (self.team * 2)) # backwards version

        self.jump_count = 0 # counts jumps; this is for double jumps and stuff
        self.kinged = False
        self.ai = main.one_player and self.team == 0 # checks if it's ai
        self.image, self.rect = img, img
        the_screen = main.pygame.display.get_surface() # get the screen variable i think
        self.area = the_screen.get_rect()

    def move_piece(self):
        # updates the y_moves
        self.y_move = self.y + (1 - (self.team * 2))
        self.jump_y_move = self.y_move + (1 - (self.team * 2))
        self.backwards_y_move = self.y + (-1 + (self.team * 2))
        self.backwards_jump_y_move = self.backwards_y_move + (-1 + (self.team * 2))

        main.ghost_pieces.clear()

        for loop_piece in main.pieces:
            loop_piece.selected = False

        self.selected = True

        can_move_left = self.x > 1 # As long as it isn't on the far left it defaults to being able to move left
        can_move_right = self.x < 8 # As long as it isn't on the far right it defaults to being able to move right
        can_move_back_left = can_move_left and self.kinged # same thing as above
        can_move_back_right = can_move_right and self.kinged
        checking_jumps = False # This is so the while loop will go around the fist time 
        # Checks if they can move
        for loop_piece in main.pieces:
            if loop_piece.x == self.x + 1 and loop_piece.y == self.y_move: # checks if there is a piece blocking the path
                can_move_right = False # makes it not able to move if theres a piece blocking the path
                if loop_piece.team != self.team and self.x + 2 <= 8 and self.jump_y_move not in [0, 9]: # if the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(2, self, self.jump_y_move) # checks if the piece in the path can be jumped

            if loop_piece.x == self.x - 1 and loop_piece.y == self.y_move:
                can_move_left = False # Makes it not able to move if theres a piece blocking the path
                if loop_piece.team != self.team and self.x - 2 >= 1 and self.jump_y_move not in [0, 9]: # If the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(-2, self, self.jump_y_move) # Checks if the piece in the path can be jumped

            if self.kinged and loop_piece.x == self.x + 1 and loop_piece.y == self.backwards_y_move:
                can_move_back_right = False # Makes it not able to move if theres a piece blocking the path
                if loop_piece.team != self.team and self.x + 2 <= 8 and self.backwards_jump_y_move not in [0, 9]: # If the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(2, self, self.backwards_jump_y_move) # Checks if the piece in the path can be jumped

            if self.kinged and loop_piece.x == self.x - 1 and loop_piece.y == self.backwards_y_move:
                can_move_back_left = False # Makes it not able to move if theres a piece blocking the path
                if loop_piece.team != self.team and self.x - 2 >= 1 and self.backwards_jump_y_move not in [0, 9]: # If the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(-2, self, self.backwards_jump_y_move) # Checks if the piece in the path can be jumped

        self.add_ghost_pieces(can_move_right, can_move_left, can_move_back_right, can_move_back_left)
        
        if self.jump_count > 0 and not checking_jumps: # if it can't jump anymore
            self.jump_count = 0
            main.turn = [1, 0][self.team]
            self.selected = False
    
    def add_ghost_pieces(self, can_move_right, can_move_left, can_move_back_right, can_move_back_left):
        if can_move_right and self.jump_count < 1: # if it can move right and it hasnt jumped
            for loop_square in main.squares: # finds the square that it's moving to
                if loop_square.x == self.x + 1 and loop_square.y == self.y_move:
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False)) # make a non-jumping ghost piece there
        
        if can_move_left and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x - 1 and loop_square.y == self.y_move:
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
        
        if can_move_back_right and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x + 1 and loop_square.y == self.backwards_y_move:
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
        
        if can_move_back_left and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x - 1 and loop_square.y == self.backwards_y_move:
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
        

    def can_be_jumped(self, x_direction, jumper, jumper_jump_y_move):
        can_jump = True # Set the default to it being able to be jumped
        if x_direction == 2: # If it's being jumped to the right
            for loop_piece in main.pieces: # Check each piece
                if loop_piece.x == self.x + 1 and loop_piece.y == jumper_jump_y_move: # If there's a piece blocking the jump
                    can_jump = False # It can't be jumped

        if x_direction == -2: # Same as above but for jumping to the left
            for loop_piece in main.pieces:
                if loop_piece.x == self.x - 1 and loop_piece.y == jumper_jump_y_move:
                    can_jump = False

        if can_jump:
            for loop_square in main.squares: # find a square the jumper is jumping to
                if loop_square.x == jumper.x + x_direction and loop_square.y == jumper_jump_y_move:
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, jumper, True, self)) # creates a jumping ghost piece


        return can_jump # If it doesn't think there's anything blocking the jump it'll return the default but if it's changed to False it'll return that


    def render(self):
        img = self.image
        if self.selected and main.turn == self.team: # if it's selected change the image
            if self.team == 0: # red stuff
                if self.kinged:
                    img = main.red_king_piece_sel_texture_path
                else:
                    img = main.red_piece_sel_texture_path
            if self.team == 1: # black stuff
                if self.kinged:
                    img = main.black_king_piece_sel_texture_path
                else:
                    img = main.black_piece_sel_texture_path
        main.screen.blit(
            main.pygame.transform.scale( # resize to fit squares
                main.pygame.image.load(img), # the images
                (main.square_size, main.square_size) # image dimensions
            ),
            ( # pixel location
                main.board_x_offset + (self.x * main.square_size),
                self.y * main.square_size
            )
        )
