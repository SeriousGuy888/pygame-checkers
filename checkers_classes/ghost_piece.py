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
        self.ghosted_piece.x = self.x
        self.ghosted_piece.y = self.y
        self.ghosted_piece.y_move = self.ghosted_piece.y_move + 1 if self.ghosted_piece.team == 0 else self.ghosted_piece.y_move - 1
        main.ghost_pieces = []
        if self.is_jumping_piece:
            self.ghosted_piece.jump_count = self.ghosted_piece.jump_count + 1
            print("ghosted jump count: " + str(self.ghosted_piece.jump_count))
            main.jumped_pieces.append(self.piece_being_jumped)
            main.pieces.remove(self.piece_being_jumped)
            self.ghosted_piece.move_piece()
            if len(main.pieces) <= 8:
                red_pieces = 0
                black_pieces = 0
                for loop_piece in main.pieces:
                    if loop_piece.team == 0:
                        red_pieces += 1
                    elif loop_piece.team == 1:
                        black_pieces += 1
                if red_pieces == 0:
                    main.winner = 1
                if black_pieces == 0:
                    main.winner = 0

        else:
            self.ghosted_piece.selected = False
            main.turn = [1, 0][self.ghosted_piece.team]
            
        if [9,1][self.ghosted_piece.team] == self.ghosted_piece.y:
            self.ghosted_piece.kinged = True
            self.ghosted_piece.image = [main.red_king_piece_texture_path, main.black_king_piece_texture_path][self.ghosted_piece.team]

    def render(self):
        main.screen.blit(
            main.pygame.transform.scale( # resize to fit squares
                main.pygame.image.load(main.ghost_piece_texture_path), # the images
                (main.square_size, main.square_size) # image dimensions
            ),
            ( # pixel location
                # int(main.SCREEN_WIDTH - (main.square_size * self.x) - ((main.SCREEN_WIDTH - (main.square_size * 8)) / 2)),
                main.board_x_offset + (self.x * main.square_size),
                self.y * main.square_size
            )
        )
