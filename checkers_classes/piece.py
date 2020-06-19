import __main__ as main

class Piece(main.pygame.sprite.Sprite):
    def __init__(self, team, square, selected):
        main.pygame.sprite.Sprite.__init__(self)

        self.square = square
        self.x = square.x
        self.y = square.y

        self.selected = selected
            
        img = [main.red_piece_texture_path, main.black_piece_texture_path][self.team]
        
        self.y_move = self.y + (1 - (self.team * 2))
        self.jump_y_move = self.y_move + (1 - (self.team * 2))
        self.backwards_y_move = self.y + (-1 + (self.team * 2))
        self.backwards_jump_y_move = self.backwards_y_move + (-1 + (self.team * 2))

        self.jump_count = 0
        self.kinged = False
        self.image, self.rect = img, img
        the_screen = main.pygame.display.get_surface() # get the screen variable i think
        self.area = the_screen.get_rect()
        self.team = team
    def is_clicked(self):
        return main.pygame.mouse.get_pressed()[0] and self.rect.collidepoint(main.pygame.mouse.get_pos())

    def move_piece(self):
        self.y_move = self.y + (1 - (self.team * 2))
        self.jump_y_move = self.y_move + (1 - (self.team * 2))
        self.backwards_y_move = self.y + (-1 + (self.team * 2))
        self.backwards_jump_y_move = self.backwards_y_move + (-1 + (self.team * 2))

        main.ghost_pieces = []
        for loop_piece in main.pieces:
            loop_piece.selected = False

        self.selected = True

        can_move_left = self.x > 1 # As long as it isn't on the far left it defaults to being able to move left
        can_move_right = self.x < 8 # As long as it isn't on the far right it defaults to being able to move right
        can_move_back_left = self.kinged
        can_move_back_right = self.kinged
        checking_jumps = False # This is so the while loop will go around the fist time 
        # Checks if they can move
        for loop_piece in main.pieces:

            if loop_piece.x == self.x + 1 and loop_piece.y == self.y_move: # checks if there is a piece blocking the path
                can_move_right = False # makes it not able to move if theres a piece blocking the path
                # print("you cant shirt box move right")
                if loop_piece.team != self.team: # if the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(2, self, self.jump_y_move) # checks if the piece in the path can be jumped

            if loop_piece.x == self.x - 1 and loop_piece.y == self.y_move:
                can_move_left = False # Makes it not able to move if theres a piece blocking the path
                # print("ytard cant move left")
                if loop_piece.team != self.team: # If the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(-2, self, self.jump_y_move) # Checks if the piece in the path can be jumped

            if self.kinged and loop_piece.x == self.x + 1 and loop_piece.y == self.backwards_y_move:
                can_move_back_right = False # Makes it not able to move if theres a piece blocking the path
                # print("ytard cant move left")
                if loop_piece.team != self.team: # If the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(2, self, self.backwards_jump_y_move) # Checks if the piece in the path can be jumped

            if self.kinged and loop_piece.x == self.x - 1 and loop_piece.y == self.backwards_y_move:
                can_move_back_left = False # Makes it not able to move if theres a piece blocking the path
                # print("ytard cant move left")
                if loop_piece.team != self.team: # If the piece that is blocking the path is on the other team, then
                    checking_jumps = loop_piece.can_be_jumped(-2, self, self.backwards_jump_y_move) # Checks if the piece in the path can be jumped

        # Draws a ghost piece if they can move right/left
        print("my jump_count: " + str(self.jump_count))
        if can_move_right and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x + 1 and loop_square.y == self.y_move:
                    # print("x = " + str(loop_square.x))
                    # print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
           
        if can_move_left and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x - 1 and loop_square.y == self.y_move:
                    # print("x = " + str(loop_square.x))
                    # print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
        
        if can_move_back_right and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x + 1 and loop_square.y == self.backwards_y_move:
                    # print("x = " + str(loop_square.x))
                    # print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
        
        if can_move_back_left and self.jump_count < 1:
            for loop_square in main.squares:
                if loop_square.x == self.x - 1 and loop_square.y == self.backwards_y_move:
                    # print("x = " + str(loop_square.x))
                    # print("y = " + str(loop_square.y))
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, self, False, False))
           

        if self.jump_count > 0 and checking_jumps == False:
            self.jump_count = 0
            main.turn = [1, 0][self.team]
            self.selected = False

    def can_be_jumped(self, x_direction, jumper, jumper_jump_y_move):
        can_jump = True # Set the default to it being able to be jumped
        if x_direction == 2: # If it's being jumped to the right
            for loop_piece in main.pieces: # Check each piece
                if loop_piece.x == self.x + 1 and loop_piece.y == jumper_jump_y_move: # If there's a piece blocking the jump
                    can_jump = False # It can't be jumped
                    # print("cant be jumped right") # This was for debugging and I might delete it

        if x_direction == -2: # Same as above but for jumping to the left
            for loop_piece in main.pieces:
                if loop_piece.x == self.x - 1 and loop_piece.y == jumper_jump_y_move:
                    can_jump = False
                    # print("cant be jumped left")

        if can_jump:
            for loop_square in main.squares:
                if loop_square.x == jumper.x + x_direction and loop_square.y == jumper_jump_y_move:
                    main.ghost_pieces.append(main.ghost_piece.GhostPiece(loop_square, jumper, True, self))


        return can_jump # If it doesn't think there's anything blocking the jump it'll return the default but if it's changed to False it'll return that


    def render(self):
        img = self.image
        if self.selected:
            if self.team == 0:
                if self.kinged:
                    img = main.red_king_piece_sel_texture_path
                else:
                    img = main.red_piece_sel_texture_path
            if self.team == 1:
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
                # int(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2)),
                main.board_x_offset + (self.x * main.square_size),
                self.y * main.square_size
            )
        )
