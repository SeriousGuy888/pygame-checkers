import __main__ as main

def spawn_sprites():
    for x in range(1, main.SQUARE_DIMENSION + 1):
        for y in range(1, main.SQUARE_DIMENSION + 1):
            if (x + (1 - y % 2)) % 2 == 1:
                square_colour = main.white_square
            if (x + (1 - y % 2)) % 2 == 0:
                square_colour = main.black_square

            main.squares.append(main.square.Square(square_colour, x, y))
    for x in range(1, 8, 2):
        for y in [1, 2, 3, 6, 7, 8]:
            x_coord = x + (y % 2)
            y_coord = y
            team = 0 if y < 5 else 1 
            for loop_square in main.squares:
                if loop_square.x == x_coord and loop_square.y == y_coord:
                    main.pieces.append(main.piece.Piece(team, loop_square, False))