import __main__ as main

class GhostPiece(main.pygame.sprite.Sprite):
    def __init__(self, square, ghosted_piece, is_jumping_piece, piece_being_jumped):
        main.pygame.sprite.Sprite.__init__(self)

        self.x = square.x
        self.y = square.y
        self.ghosted_piece = ghosted_piece
        self.is_jumping_piece = is_jumping_piece
        self.piece_being_jumped = piece_being_jumped

    def move_ghosted_piece(self):
        self.ghosted_piece.x = self.x # move the ghosted piece to the ghost piece
        self.ghosted_piece.y = self.y
        # self.ghosted_piece.y_move = self.ghosted_piece.y_move + 1 if self.ghosted_piece.team == 0 else self.ghosted_piece.y_move - 1 
        main.ghost_pieces = [] # gets rid of all ghost pieces
        if self.is_jumping_piece: # if this is for a jump
            self.ghosted_piece.jump_count = self.ghosted_piece.jump_count + 1 # increases the ghosted pieces's jump count
            [main.red_jumped_pieces, main.black_jumped_pieces][self.piece_being_jumped.team].append(self.piece_being_jumped) # adds to dead piece list
            main.pieces.remove(self.piece_being_jumped) # kills jumped piece
            self.ghosted_piece.move_piece() # moves piece again; this is for double jumps and checking if it can't jump anymore
            if len(main.pieces) <= 12: # when it's possible that a team is gone, checks if a team has won
                red_pieces = 0 # for counting red pieces
                black_pieces = 0 # for counting black pieces
                for loop_piece in main.pieces: # adds to the piece counts
                    if loop_piece.team == 0:
                        red_pieces += 1
                    elif loop_piece.team == 1:
                        black_pieces += 1
                if red_pieces == 0: # if a team han no pieces the other team wins
                    main.winner = 1
                if black_pieces == 0:
                    main.winner = 0

        else: # if it's not jumping
            self.ghosted_piece.selected = False # deselect piece
            main.turn = [1, 0][self.ghosted_piece.team] # other team's turn
            
        if [8, 1][self.ghosted_piece.team] == self.ghosted_piece.y and not self.ghosted_piece.kinged: # if in a spot to be kinged
            main.pygame.mixer.Sound.play(main.random.choice(main.king_sounds))
            self.ghosted_piece.kinged = True # king it
            self.ghosted_piece.image = [main.red_king_piece_texture_path, main.black_king_piece_texture_path][self.ghosted_piece.team] # change image

    def render(self):
        main.screen.blit(
            main.pygame.transform.scale( # resize to fit squares
                main.pygame.image.load(main.ghost_piece_texture_path), # the images
                (main.square_size, main.square_size) # image dimensions
            ),
            ( # pixel location
                main.board_x_offset + (self.x * main.square_size),
                self.y * main.square_size
            )
        )
